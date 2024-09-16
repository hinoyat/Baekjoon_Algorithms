import heapq, sys
input = sys.stdin.readline

def supernova(start, end):
    visited = [3300000] * (V + 1)
    que = [(0, start)]
    visited[start] = 0
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

    return visited

V, E = map(int, input().split())
start = int(input())
end = V
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    v1, v2, val = map(int, input().split())
    graph[v1].append((val, v2))



result = supernova(start, V)

for i in range(1, V + 1):
    if result[i] == 3300000:
        print('INF')
        continue

    print(result[i])