N = int(input())

DP = [0] * (N + 1)

time = []
money = []
for _ in range(N):
    t, m = map(int, input().split())
    time.append(t)
    money.append(m)

for i in range(N):
    # 현재까까까까까꺅지 최댓값
    DP[i] = max(DP[i - 1], DP[i])
    
    # 자 미래의 최댓값을 넣어보자
    if i + time[i] <= N:
        # 일단 시간이 된다면 해봐라 근데 누구랑 비교해야 하나?
        # 누구랑 비교하긴 원래 있던 값이랑 해야지
        DP[i + time[i]] = max(DP[i] + money[i], DP[i + time[i]])
    # print(i)
    # print(DP)

print(max(DP))