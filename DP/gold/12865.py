def DP(w, v):
    dp = [[0] * (M + 1) for _ in range(N+1)]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if w[i-1] <= j:
                dp[i][j] = max(v[i-1] + dp[i-1][j - w[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[N][M]


N, M = map(int, input().split())
weight = [0] * N
value = [0] * N
for i in range(N):
    w, v = map(int, input().split())
    weight[i] = w
    value[i] = v
print(DP(weight, value))