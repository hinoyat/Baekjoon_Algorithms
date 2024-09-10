def find_mother(people):
    if people != parent[people]:
        people = find_mother(parent[people])

    return people

def make_family(a, b):
    a = find_mother(a)
    b = find_mother(b)

    if a == b:
        return

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
while (N, M) != (0, 0):
    graph = []
    parent = [i for i in range(N + 1)]

    max_len = 0
    for _ in range(M):
        c1, c2, clen = map(int, input().split())
        graph.append((clen, c1, c2))
        max_len += clen
    graph.sort()

    min_len = 0
    for clen, c1, c2 in graph:
        if find_mother(c1) != find_mother(c2):
            make_family(c1, c2)
            min_len += clen
    print(max_len - min_len)

    N, M = map(int, input().split())
