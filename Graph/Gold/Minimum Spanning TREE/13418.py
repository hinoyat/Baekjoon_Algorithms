import sys
input = sys.stdin.readline
def find(c):
    if c != parent[c]:
        parent[c] = find(parent[c])

    return parent[c]


def make(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


N, M = map(int, input().split())

parent = [i for i in range(N + 1)]
graph = []

for _ in range(M+1):
    c1, c2, v = map(int,input().split())
    graph.append(((v + 1)%2, c1, c2))
# print(graph)
max_v = 0
graph.sort(reverse=True)
for v, c1, c2 in graph:
    if find(c1) != find(c2):
        make(c1, c2)
        max_v += v

parent = [i for i in range(N + 1)]
graph.sort()
min_v = 0
for v, c1, c2 in graph:
    if find(c1) != find(c2):
        make(c1, c2)
        min_v += v
# print(max_v, min_v)
print((max_v**2)-(min_v**2))
