# 벽부수고 이동하기
import pprint
from collections import deque


def supernova(si, sj):
    que = deque()
    # 좌표1, 좌표2, 벽 부순 여부
    que.append((si, sj, 0))
    # 방문 여부 부순 여부
    visited = [[[0 for _ in range(2)] for _ in range(M)] for _ in range(N)]
    visited[si][sj][0] = 1
    while que:
        qi, qj, boom = que.popleft()
        if (qi, qj) == (N-1, M-1):
            return visited[qi][qj][boom]

        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if 0<= ni < N and 0<= nj < M:
                if arr[ni][nj] == '1' and boom == 0:
                    visited[ni][nj][1] = visited[qi][qj][0] + 1
                    que.append((ni, nj, 1))
                elif arr[ni][nj] == '0' and visited[ni][nj][boom] == 0:
                    visited[ni][nj][boom] = visited[qi][qj][boom] + 1
                    que.append((ni, nj, boom))
    return -1


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
start = (0, 0)
end = (N-1, M-1)
print(supernova(0, 0))