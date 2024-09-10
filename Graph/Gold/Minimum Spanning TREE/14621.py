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
info = [0] + list(map(str, input().split()))

parent = [i for i in range(N + 1)]
graph = []
for _ in range(M):
    c1, c2, val = map(int, input().split())
    graph.append((val, c1, c2))
graph.sort()
ans = 0
cnt = 0
for val, c1, c2 in graph:
    if info[c1] == info[c2]:
        continue
    if find(c1) != find(c2):
        make(c1, c2)
        ans += val
        cnt += 1
if cnt == N - 1:
    print(ans)
else:
    print(-1)

'''
5 7
W W W W M
1 2 12
1 3 10
4 2 5
5 2 5
2 5 10
3 4 3
5 4 7
'''