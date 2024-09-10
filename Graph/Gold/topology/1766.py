# 1766 문제집 위상 정렬 + heapq

import heapq
import sys
input = sys.stdin.readline
def supernova():
    result = []

    que = []

    for i in range(1, N + 1):
        if check[i] == 0:
            heapq.heappush(que, i)
    while que:
        q = heapq.heappop(que)
        result.append(q)
        for j in graph[q]:
            check[j] -= 1
            if check[j] == 0:
                heapq.heappush(que, j)
    print(*result)


N, M = map(int, input().split())

check = [0] * (N + 1)
graph = [[]for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    check[v2] += 1
supernova()
