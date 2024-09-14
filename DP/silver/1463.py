# 1로 만들기

# 조건

# 조건 1 3으로 나누어 떨어지면 3으로 나눈다
# 조건 2 2로 나누어 떨어지면 2으로 나눈다
# 조건 3 1을 뺀다

import sys
input = sys.stdin.readline

N = int(input())
DP = [0] * ((N + 1) * 2)
DP[0] = 1
DP[1] = 0
DP[2] = 1
DP[3] = 2
# [0, 0, 0, 0, 0]
for i in range(3, N + 1):
    DP[i] = DP[i-1] + 1
    if i % 2 == 0:
        DP[i] = min(DP[i//2] + 1, DP[i])
    if i % 3 == 0:
        DP[i] = min(DP[i//3] + 1, DP[i])
        # print(DP)

# print(DP)
print(DP[N])
