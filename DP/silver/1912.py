N = int(input())

num = list(map(int, input().split()))
bbibbi = [-1111] * (N + 1)
for i in range(1, N + 1):
    bbibbi[i] = max(num[i-1], bbibbi[i-1] + num[i-1])
print(max(bbibbi))
