import sys, heapq
input = sys.stdin.readline

def supernova(start, end):
    visited = [float('inf')] * (N + 1)
    que = [(0, start)]
    visited[start] = 0

    while que:
        val, q = heapq.heappop(que)
        if visited[q] < val:continue
        for nv, nq in graph[q]:
            nval = val + nv
            if nval < visited[nq]:
                visited[nq] = nval
                heapq.heappush(que, (nval, nq))

    return visited[end]


N = int(input())
M = int(input())
graph = [[]for _ in range(N + 1)]

for _ in range(M):
    v1, v2, val = map(int, input().split())
    graph[v1].append((val, v2))

start, end = map(int, input().split())

print(supernova(start, end))