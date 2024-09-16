import heapq, sys
input = sys.stdin.readline

def supernova(start, end, graph):
    visited = [1000100] * (N + 1)
    que = [(0, end)]
    visited[end] = 0
    while que:
        v, q = heapq.heappop(que)
        if v > visited[q]:
            continue
        for nv, nq in graph[q]:
            newv = v + nv
            if newv > visited[nq]:
                continue
            visited[nq] = newv
            heapq.heappush(que, (newv, nq))


    return visited[1:]

N, M, X = map(int, input().split())

go_graph = [[]for _ in range(N+1)]
back_graph = [[]for _ in range(N+1)]

for _ in range(M):
    v1, v2, val = map(int, input().split())
    go_graph[v1].append((val, v2))
    back_graph[v2].append((val, v1))

go_result = supernova(N, X, go_graph)
back_result = supernova(N, X, back_graph)
# print(go_result)
# print(back_result)

ans = 0
for i in range(N):
    val = go_result[i] + back_result[i]
    ans = max(val, ans)
print(ans)