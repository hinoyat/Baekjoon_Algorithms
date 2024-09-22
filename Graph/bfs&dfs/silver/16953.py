from collections import deque


def BFS(num, target):
    que = deque()
    que.append((num, 1))
    # visited = [0] * (10**9 + 1)
    min_v = 999999999
    while que:
        n, c = que.popleft()
        if n == target:
            return c
        if n * 2 <= target:
            que.append((n*2, c + 1))
        if n * 10 + 1 <= target:
            que.append((n * 10 + 1, c + 1))
    return -1



N, target = map(int, input().split())

print(BFS(N, target))