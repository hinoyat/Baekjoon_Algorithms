def find(c):
    while parent[c] != c:
        c = parent[c]

    return c


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if parent[a] > parent[b]:
        parent[a] = b
    else:
        parent[b] = a


import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = [ i for i in range(N + 1)]
Graph = []

for i in range(M):
    a, b, c = map(int, input().split())
    Graph.append((c, a, b))

Graph.sort()
ans = 0



for val, A, B in Graph:

    A = find(A)
    B = find(B)

    if A == B:
        continue
    else:
        union(A, B)
        ans += val
print(ans)