import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    global ans
    que = []
    heapq.heappush(que, (0, start))
    visited = [0xffff] * (N+1)
    visited[start] = 0
    while que:
        # 힙큐에서는 거리를 관리
        cur_dis, que_node = heapq.heappop(que)
        if cur_dis > visited[que_node]:continue
        for dis, node in graph[que_node]:
            newdis = cur_dis + dis
            if newdis < visited[node]:
                visited[node] = newdis
                heapq.heappush(que, (newdis, node))
    temp = 0
    for v in range(1, N+1):
        if visited[v] <=M:
            temp += items[v]
    # print(visited)
    return temp


N, M, R = map(int, input().split())

items = [0] + list(map(int, input().split()))

ans = 0

graph = [[]for _ in range(N+1)]

for _ in range(R):
    a, b, val = map(int, input().split())
    graph[a].append((val, b))
    graph[b].append((val, a))

for r in range(1, N+1):
    ans = max(dijkstra(r), ans)
# print(graph)
print(ans)


