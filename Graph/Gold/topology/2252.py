# 2252 줄 세우기  위상 정렬

from collections import deque
# import sys
# input = sys.stdin.readline
def supernova():
    result = []
    que = deque()

    for i in range(1, N + 1):
        if check[i] == 0:
            que.append(i)


    while que:
        q = que.popleft()
        result.append(q)

        for p in graph[q]:
            check[p] -= 1
            if check[p] == 0:
                que.append(p)

    print(*result)

N, M = map(int, input().split())
check = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    check[v2] += 1

supernova()