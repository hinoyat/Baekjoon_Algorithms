from itertools import combinations
from collections import deque
def BFS(viruspoint):
    min_visit = 21e8
    # 벽을 세우는 조합 생성
    for c1 in list(combinations(notwall, 3)):
        visited = [[0]*M for _ in range(N)]
        # 사라진 안전한 공간
        cnt = 0
        # 조합에서 뽑은 곳에
        # 벽 설치
        for c2 in c1:
            wi, wj = c2
            visited[wi][wj] = 1
            cnt += 1
        que = deque()
        # 바이러스가 퍼진 수
        # 바이러스는 방문 처리
        for v in viruspoint:
            que.append([v[0], v[1]])
            visited[v[0]][v[1]] = 1
        while que:
            vi, vj = que.popleft()
            # 바이러스가 갈 수 있는 곳
            for pi, pj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                ni = vi + pi
                nj = vj + pj
                if 0<=ni<N and 0<=nj<M and lab[ni][nj]==0 and visited[ni][nj]==0:
                    que.append([ni,nj])
                    visited[ni][nj] = 1
                    # 퍼질 때마다 1씩 증가 => 사라지는 안전한 공간
                    cnt += 1
                # 더하다가 이전 경우보다 많이 퍼지면 다른 경우 들어가기
            if cnt > min_visit:
                break
        # 지금까지 최소로 퍼졌다면 max 값 갱신
        if cnt < min_visit:
            min_visit = cnt

    return min_visit


N, M = map(int, input().split())
lab = [list(map(int, input().split()))for _ in range(N)]

# 안전한 공간 # 조합 뽑을 때 필요
notwall = []

# 바이러스 시작점
viruspoint = []

# 안전한 공간
wallcnt = 0
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            notwall.append([i,j])
            wallcnt += 1
        if lab[i][j] == 2:
            viruspoint.append([i,j])
print(f'{wallcnt - BFS(viruspoint)}')
