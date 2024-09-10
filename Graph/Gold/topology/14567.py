'''
# A 형에서 -1
3 2
1 1
1 2


'''



from collections import deque
import sys
input = sys.stdin.readline
def topology():
    result = [1] * (N+1)
    que = deque()

    cnt = 0

    for i in range(1, N + 1):
        if check[i] == 0:
            que.append(i)

    while que:
        q = que.popleft()
        for point in graph[q]:
            check[point] -= 1
            if check[point] == 0:
                que.append(point)
            result[point] = result[q] + 1

    return print(*result[1:])





N, M = map(int, input().split())


check = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    check[v2] += 1

topology()

