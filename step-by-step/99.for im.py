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


# # 13300 방 배정

# N, K = map(int, input().split())
# lst = []
# dct = {}
# for _ in range(N):
#     S_Y = tuple(map(int, input().split()))
#     lst.append(S_Y)

# for i in lst:
#     if i not in dct :
#         dct[i] = 1
#     else:
#         dct[i] += 1

# room = 0
# for d in dct.keys():
#     room += dct[d]//K
#     if dct[d] %  K >0:
#         room += 1

# print(room)


# # 2605 줄 세우기
# N = int(input())
# stdnt = [i for i in range(1, N+1)]

# num = list(map(int, input().split()))

# for i in range(N):
#     if num[i] == 0:
#         pass
#     else:
#         for j in range(num[i]):
#             stdnt[i-num[i]+j], stdnt[i] = stdnt[i], stdnt[i-num[i]+j]
# print(*stdnt)

# # 14696 딱지놀이
# N = int(input())
# for round in range(1, N+1):
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     a_num = A.pop(0)
#     b_num = B.pop(0)
#     # print(A, a_num)
#     # print(B, b_num)

#     winner = 'D'

#     for i in range(4, 0, -1):
#         if A.count(i) > B.count(i):
#             winner = 'A'
#             break
#         elif A.count(i) < B.count(i):
#             winner = 'B'
#             break
#         else:
#             pass
#     print(winner)

# # 2628 종이 자르기

# row, col = map(int, input().split())
# N = int(input())

# r_lst = []
# c_lst = []

# for cut in range(N):
#     r_c, num = map(int, input().split())
#     if r_c == 0:
#         c_lst.append(num)
#     else:
#         r_lst.append(num)

# row_lst = [0] + r_lst + [row]
# col_lst = [0] + c_lst + [col]


# row_lst.sort()
# col_lst.sort()

# max_row = 0
# max_col = 0
# # 행 길이 최댓값
# for i in range(len(row_lst)-1):
#     if row_lst[i+1] - row_lst[i] > max_row:
#         max_row = row_lst[i+1] - row_lst[i]
# # 열 길이 최댓값
# for j in range(len(col_lst)-1):
#     if col_lst[j+1] - col_lst[j] > max_col:
#         max_col = col_lst[j+1] - col_lst[j]


# result = max_row * max_col

# print(result)


# # 2578 비잉고오
# arr_a = [list(map(int, input().split())) for _ in range(5)]

# lst_b = []
# for b in range(5):
#     b = list(map(int, input().split()))
#     for b_1 in b:
#         lst_b.append(b_1)


# cnt = 0
# b_idx = 0
# ar1 = 0
# ar2 = 0
# ar3 = 0
# ar4 = 0


# binggo = False
# while binggo == False:
#         cnt += 1
#         num = lst_b[b_idx]
#         for i in range(5):
#             for j in range(5):
#                 if arr_a[i][j] == num:
#                     arr_a[i][j] = 0

#         b_idx += 1
#         # 행 합
#         for i in range(5):
#             if sum(arr_a[i]) == 0:
#                 ar1 += 1

#         # 열 합
#         for i in range(5):
#             sum2 = 0
#             for j in range(5):
#                 sum2 += arr_a[j][i]
#             if sum2 == 0:
#                 ar2 +=1
#         # 대각
#         sum3 = 0
#         for i in range(5):
#             for j in range(5):
#                 if i==j:
#                     sum3 += arr_a[i][j]
#         if sum3 == 0:
#             ar3 +=1

#         # 역대각
#         sum4 = 0
#         for i in range(5):
#             for j in range(5):
#                 if 5-i-1==j:
#                     sum4 += arr_a[i][j]
#         if sum4 == 0:
#             ar4 +=1

#         # 종료        
#         if ar1 + ar2 + ar3 + ar4 >= 3:
#             binggo = True
#         else:
#             ar1 = ar2 = ar3 = ar4 = 0

# # print(binggo, cnt)
# # print(ar1, ar2, ar3, ar4)
# # pprint(arr_a)
# print(cnt)

    
# # pprint(arr_a)
