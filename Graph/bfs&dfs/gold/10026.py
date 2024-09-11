from collections import deque
import sys
input = sys.stdin.readline

def BFS(si, sj):
    que = deque()
    que.append([si, sj])
    visited[si][sj] = 1
    word = arr[si][sj]
    while que:
        qi, qj = que.popleft()
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N or visited[ni][nj] or arr[ni][nj] != word:
                continue
            visited[ni][nj] = 1
            que.append((ni, nj))

N = int(input())

arr = [list(input()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
ans1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j)
            ans1 += 1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

visited = [[0] * N for _ in range(N)]
ans2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j)
            ans2 += 1

print(ans1, ans2)