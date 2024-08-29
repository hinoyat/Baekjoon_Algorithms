# 좌표 압축
N = int(input())
dct = {}

num = list(map(int, input().split()))
set1 = set(num)
s = list(set1)
s.sort()
v = 0
for i in s:
    dct[i] = v
    v += 1

for j in num:
    print(f'{dct[j]}', end=' ')