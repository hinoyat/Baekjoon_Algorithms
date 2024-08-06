from pprint import pprint


# # 2309 일곱 난쟁이
# N = 9
# dwarf_lst = []
# for _ in range(N):
#     dwarf = int(input())
#     dwarf_lst.append(dwarf)

# dwarf_sum = 100

# cur_sum = sum(dwarf_lst)

# pop_lst = []
# for i in range(N):
#     for j in range(N):
#         if i != j:
#             if cur_sum - dwarf_lst[i] - dwarf_lst[j] == dwarf_sum:
#                 if len(pop_lst) <2:
#                     pop_lst.append(i)
#                     pop_lst.append(j)
                    

# pop_set = set(pop_lst)

# real_dwarf = []
# for s in range(N):
#     if s not in pop_lst:
#         real_dwarf.append(dwarf_lst[s])

# real_dwarf.sort()

# for d in real_dwarf:
#     print(d)



# # 10163 색종이
# import sys
# input = sys.stdin.readline
# N = int(input())

# arr = [[0 for _ in range(1001)]for _ in range(1001)]
# for a in range(1, N+1):
#     x1, y1, x_len, y_len = map(int, input().split())
#     for i in range(x1, x1 + x_len):
#         for j in range(y1, y1 + y_len):
#             arr[i][j] = a
# cnt_lst = []

# for cnt in range(1, N+1):
#     sum_cnt = 0
#     for i in arr:
#         sum_cnt += i.count(cnt)
#     cnt_lst.append(sum_cnt)

# for c in cnt_lst:
#     print(c)


# 13300 방 배정

N, K = map(int, input().split())
lst = []
dct = {}
for _ in range(N):
    S_Y = tuple(map(int, input().split()))
    lst.append(S_Y)

for i in lst:
    if i not in dct :
        dct[i] = 1
    else:
        dct[i] += 1

