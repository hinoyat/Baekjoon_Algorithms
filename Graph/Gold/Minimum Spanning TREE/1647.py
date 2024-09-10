def find(c):
    if parent[c] != c:
        parent[c] = find(parent[c])
    return parent[c]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

graph.sort(key=lambda x: x[2])

ans = 0
end = 0
for a, b, cost in graph:
    a = find(a)
    b = find(b)
    if a == b:
        continue
    if a != b:
        union(a, b)
        ans += cost
        end = cost

print(ans - end)