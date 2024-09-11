from pprint import pprint
# 2178 미로 탐색
def BFS(si, sj, endi, endj):
    visited = [[0] * M  for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    que = []
    que.append([si, sj])
    visited[si][sj] = 1
    # pprint(visited)
    result = []
    cnt = 0
    while que:
        pi, pj = que.pop(0)
        if pi == endi and pj == endj:
            result = visited[pi][pj]
            break
        else:
            for d in range(4):
                ni = pi + di[d]
                nj = pj + dj[d]
                if 0<= ni < N and 0<= nj < M and arr[ni][nj] !='0' and visited[ni][nj] < 1:
                    que.append([ni, nj])
                    cnt += 1
                    # print(cnt)
                    # print(que)
                    visited[ni][nj] = visited[pi][pj] + 1

    return result
          
    

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# pprint(arr)
si = 0
sj = 0
endi = N-1
endj = M-1
print(BFS(si, sj, endi, endj))
