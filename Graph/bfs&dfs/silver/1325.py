from collections import deque
import sys
input = sys.stdin.readline


def supernova(start):
    cnt = 1
    visited = [0] * (N+1)
    que = deque()
    que.append(start)
    visited[start] = 1
    while que:
        q = que.popleft()
        for v in graph[q]:
            if not visited[v]:
                visited[v] = 1
                que.append(v)
                cnt += 1
    return cnt

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
# print(graph)
max_hack = 0
result = []
for i in range(1, N + 1):
        c = supernova(i)
        if c > max_hack:
            max_hack = c
            result.clear()
            result.append(i)
        elif c == max_hack:
            result.append(i)
result.sort()
print(*result)