# 1005 ACM Craft  위상 정렬  + DP

from collections import deque
import sys
input = sys.stdin.readline
def supernova(goal):
    dp = [0] * 1001
    que = deque()

    for i in range(1, N + 1):
        if check[i] == 0:
            que.append(i)
            dp[i] = time_lst[i - 1]

    while que:
        q = que.popleft()
        for v in graph[q]:
            check[v] -= 1
            dp[v] = max(dp[v], dp[q] + time_lst[v -1])
            if check[v] == 0:
                que.append(v)
    return dp[goal]




T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    time_lst = list(map(int, input().split()))
    check = [0] * (N + 1)
    graph = [[]for _ in range(N+1)]
    for _ in range(K):
        v1, v2 = map(int, input().split())
        check[v2] += 1
        graph[v1].append(v2)
    goal = int(input())
    print(supernova(goal))