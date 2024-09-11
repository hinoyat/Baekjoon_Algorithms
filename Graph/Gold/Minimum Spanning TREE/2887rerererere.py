import sys
input = sys.stdin.readline

def find(c):
    if c != parent[c]:
        parent[c] = find(parent[c])

    return parent[c]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if parent[a] > parent[b]:
        parent[a] = b
    else:
        parent[b] = a

N = int(input())

X_info = []
Y_info = []
Z_info = []
parent = [i for i in range(N)]
graph = []

for _ in range(N):
    x, y, z = map(int, input().split())
    X_info.append(x)
    Y_info.append(y)
    Z_info.append(z)

for i in range(N - 1):
    for j in range(i + 1, N):
        graph.append((min(abs(X_info[i] - X_info[j]), abs(Y_info[i] - Y_info[j]), abs(Z_info[i] - Z_info[j])), i, j))
# print(graph)
graph.sort()
ans = 0
for v, c1, c2 in graph:
    if find(c1) != find(c2):
        union(c1, c2)
        ans += v
print(ans)