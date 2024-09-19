N = int(input())
d1 = [0] * N
d2 = [0] * N
for i in range(N):
    o1, o2 = map(int,input().split())
    d1[i] = o1
    d2[i] = o2

ans = 0xffffff
for i in range(1, 1<<N):
    r1 = 1
    r2 = 0
    for j in range(N):
        if (i & 1 << j):
            r1 *= d1[j]
            r2 += d2[j]

    ans = min(ans, abs(r1 - r2))
print(ans)