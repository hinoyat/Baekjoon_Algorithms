from collections import deque
import sys
input = sys.stdin.readline

def BFS(sp):
    visited = [[-1] * m for _ in range(n)]
    que = deque()
    si, sj = sp
    que.append([si, sj])
    visited[si][sj] = 0
    while que:
        qi, qj = que.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = qi + di
            nj = qj + dj
            if 0<= ni <n and 0<= nj < m and visited[ni][nj] == -1 and arr[ni][nj] != 0:
                visited[ni][nj] = visited[qi][qj] + 1
                que.append([ni, nj])

    return visited

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

sp = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            sp = [i, j]
            break
    if sp != 0:
        break

result = BFS(sp)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            result[i][j] = 0

for i in result:
    print(*i)