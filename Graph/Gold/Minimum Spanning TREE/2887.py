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

for p in range(N):
    x, y, z = map(int, input().split())
    X_info.append((x, p))
    Y_info.append((y, p))
    Z_info.append((z, p))

X_info.sort()
Y_info.sort()
Z_info.sort()
for i in range(N - 1):
    # graph.append((min(abs(X_info[i][0] - X_info[i + 1][0]), abs(Y_info[i][0] - Y_info[i + 1][0]), abs(Z_info[i][0] - Z_info[i + 1][0])), i, i + 1))
    graph.append((abs(X_info[i][0] - X_info[i + 1][0]), X_info[i][1], X_info[i+1][1]))
    graph.append((abs(Y_info[i][0] - Y_info[i + 1][0]), Y_info[i][1], Y_info[i+1][1]))
    graph.append((abs(Z_info[i][0] - Z_info[i + 1][0]), Z_info[i][1], Z_info[i+1][1]))

graph.sort()
ans = 0
for v, c1, c2 in graph:
    if find(c1) != find(c2):
        union(c1, c2)
        ans += v
print(ans)