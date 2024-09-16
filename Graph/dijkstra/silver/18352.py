import sys, heapq
input = sys.stdin.readline
def grp(start):
    result = []
    que = []
    visited = [-1] * (N + 1)
    visited[start] = 0
    heapq.heappush(que, (0, start))
    while que:
        qval, qnode = heapq.heappop(que)
        if qval == K:
            result.append(qnode)
            continue
        for nnode in graph[qnode]:
            newval = qval + 1
            if visited[nnode] == - 1:
                visited[nnode] = newval
                heapq.heappush(que, (newval, nnode))
    return result

N, M, K, X = map(int,input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)

r = grp(X)
r.sort()
if not r:
    print(-1)
else:
    for r1 in r:
        print(r1)