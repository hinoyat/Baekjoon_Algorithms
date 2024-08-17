def DFS(start, N, lst):
    visited = [0 for _ in range(N+1)]
    stack = []
    stack.append(start)
    result = []
    while stack:
        point = stack.pop()
        if visited[point]==0:
            visited[point] = 1
            result.append(point)

        for i in reversed(lst[point]):
            if visited[i] == 0:
                stack.append(i)

    return result
    
def BFS(start, N, lst):
    visited = [0 for _ in range(N+1)]
    que = []
    que.append(start)
    result2 = []
    while que:
        point = que.pop(0)
        if visited[point]==0:
            visited[point] = 1
            result2.append(point)

        for i in lst[point]:
            if visited[i] == 0:
                que.append(i)

    return result2




N, M, V = map(int, input().split())
lst = [[]for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    lst[v1].append(v2)
    lst[v2].append(v1)
for i in lst:
    i.sort()

print(lst)
dfs_r = DFS(V, N, lst)
bfs_r = BFS(V, N, lst)
print(*dfs_r)
print(*bfs_r)