# import sys
# input = sys.stdin.readline
# N = int(input())
# dp = [0 for _ in range(N + 1)]
# for i in range(1, N + 1):
#     t, m = map(int, input().split())
#     dp[i] = max(dp[i-1], dp[i])
#     if t + i <= N + 1:
#         dp[i + t - 1] = max(m + dp[i-1], dp[i + t - 1])
# print(dp[-1])
#
#
# import sys
# sys.stdin = open('input.txt', 'r')

