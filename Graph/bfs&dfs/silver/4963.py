from collections import deque
import sys
input = sys.stdin.readline


def BFS(si, sj):
    que = deque()
    que.append((si, sj))
    visited[si][sj] = 1

    while que:
        qi, qj = que.popleft()
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            ni, nj = qi + di, qj + dj
            if 0<= ni < h and 0 <= nj < w and not visited[ni][nj] and island[ni][nj] == 1:
                visited[ni][nj] = 1
                que.append((ni, nj))



w, h = map(int, input().split())
while (w, h) != (0, 0):
    island = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    ans = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and island[i][j] == 1:
                BFS(i, j)
                ans += 1
    print(ans)



    w, h = map(int, input().split())
