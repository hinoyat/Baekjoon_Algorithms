# 숫자카드
M = int(input())
d_lst = list(map(int,input().split()))
N = int(input())
s_lst = list(map(int,input().split()))

dct = {}
for i in d_lst:
    dct[i] = 0

for i in s_lst:
    if i in dct:
        print(1, end=' ')
    else:
        print(0, end=' ')