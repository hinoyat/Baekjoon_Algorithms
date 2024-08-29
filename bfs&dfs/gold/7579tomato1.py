# 토마토1
from collections import deque
import sys
input = sys.stdin.readline

def BFS():
    visited = [[-1]*(col) for _ in range(row)]
    que = deque()
    for i in range(row):
        for j in range(col):
            if arr[i][j] == 1:
                que.append([i,j])
                visited[i][j] = 0
            if arr[i][j] == -1:
                visited[i][j] = 0
    max_v = 0
    while que:
        qi, qj = que.popleft()
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni = qi + di
            nj = qj + dj
            if 0 <= ni < row and 0 <= nj < col and visited[ni][nj] == -1 and arr[ni][nj] == 0:
                que.append([ni,nj])
                visited[ni][nj] = visited[qi][qj] + 1
                if visited[ni][nj] > max_v:
                    max_v = visited[ni][nj]
    for n in visited:
        if -1 in n:
            return -1

    return max_v


col, row = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
print((BFS()))
