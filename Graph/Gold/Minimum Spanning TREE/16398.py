import sys
input = sys.stdin.readline
def findmama(c):
    if c != parent[c]:
        parent[c] = findmama(parent[c])
    return parent[c]

def makefamily(a, b):
    a = findmama(a)
    b = findmama(b)

    if a == b:
        return
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


N = int(input())

parent = [i for i in range(N + 1)]
graph = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(i + 1, N):
        graph.append((arr[j], i + 1, j + 1))


# print(graph)
graph.sort()

ans = 0
check = set()
for val, c1, c2 in graph:
    if findmama(c1) != findmama(c2):
        makefamily(c1, c2)
        ans += val
print(ans)