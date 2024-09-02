from collections import deque
import sys
input = sys.stdin.readline

def supernova():
    visited = [[0] * M for _ in range(N)]
    q = deque()
    result = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                q.append([i, j])
                visited[i][j] = 1
                result += 1
                while q:
                    qi, qj = q.popleft()
                    for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                        ni = qi + di
                        nj = qj + dj
                        if 0<= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                            q.append([ni, nj])
                            visited[ni][nj] = 1
    return result



T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    print(supernova())