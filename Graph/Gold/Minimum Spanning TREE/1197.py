# 1197 . 최소 스피닝 트리
import heapq
import sys
input = sys.stdin.readline

def siuuu():

    visited = [0] * (V + 1)
    que = [(0, 1)]
    result = 0
    while que:
        val, qv = heapq.heappop(que)
        if not visited[qv]:
            visited[qv] = 1
            result += val
            for v in graph[qv]:
                heapq.heappush(que, v)
    print(result)

V, E = map(int, input().split())

graph = [[]for _ in range(V + 1)]
visited = [0] * (V+1)

for i in range(E):
    v1, v2, val = map(int, input().split())
    graph[v1].append((val, v2))
    graph[v2].append((val, v1))
# print(graph)
siuuu()

# 유니온 파인드 버전
