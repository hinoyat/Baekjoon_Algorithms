# 1516 게임 개발 위상 정렬//
from collections import deque
import sys
input = sys.stdin.readline

def supernova():
    dp = [0] * (N + 1)
    que = deque()

    for s in range(1, N + 1):
        if check[s] == 0:
            que.append(s)
            dp[s] = times[s]

    while que:
        q = que.popleft()
        for building in graph[q]:
            check[building] -= 1
            # print(dp[building], dp[q]+ times[building])

            dp[building] = max(dp[building], dp[q] + times[building])
            if check[building] == 0:
                que.append(building)

    dp.pop(0)
    for i in dp:
        print(i)
    # print(dp)




N = int(input())
check = [0] * (N + 1)
times = [0] * (N + 1)
graph = [[]for _ in range(N+1)]
for i in range(1, N+1):
    info = list(map(int, input().split()))
    for v in range(1, len(info)):
        if info[v] != -1:
            check[i] += 1
            graph[info[v]].append(i)
    times[i] = info[0]
# print(check)
supernova()

# print(graph)
# print(times)