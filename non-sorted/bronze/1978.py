N = int(input())
lst = list(map(int, input().split()))
cnt = 0
for i in lst:
    for x in range(2, i+1):
        if i % x == 0:
            if x == i:
                cnt += 1
            break

print(cnt)