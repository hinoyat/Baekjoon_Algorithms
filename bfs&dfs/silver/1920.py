# 수 찾기
N = int(input())
N_lst = list(map(int, input().split()))
M = int(input())
M_lst = list(map(int, input().split()))

dct = {}
for i in N_lst:
    dct[i] = 1
# print(dct)

for i in M_lst:
    if i in dct:
        print(dct[i])
    else:
        print(0)