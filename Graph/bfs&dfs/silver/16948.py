# 데스나이트
from collections import deque
def death(sr, sc, endi, endj):
    que = deque()
    visited = [[0] * N for _ in range(N)]
    que.append((sr, sc, 0))
    visited[sr][sc] = 1
    ans = 0
    while que:
        r, c, cnt = que.popleft()
        if (r, c) == (endi, endj):
            return cnt
        for ni, nj in (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1):
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = 1
                que.append((ni, nj, cnt + 1))
    return -1

N = int(input())

arr = []
# 0번부터 시작하니 그냥 쓰자요
r1, c1, r2, c2 = map(int, input().split())

print(death(r1, c1, r2, c2))