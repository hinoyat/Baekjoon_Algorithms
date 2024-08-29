N, K = map(int,input().split())
lst = list(map(int, input().split()))

max_t = -21e8
for i in range(N-K+1):
    sum_v = 0
    for j in range(i, i+K):
        sum_v += lst[j]
    if sum_v > max_t:
        max_t = sum_v
print(max_t)