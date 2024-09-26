T = int(input())
for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    money = 0
    target = lst[-1]
    for i in range(N-2, -1, -1):
        if lst[i] < target:
            money += target - lst[i]
        else:
            target = lst[i]
    print(money)