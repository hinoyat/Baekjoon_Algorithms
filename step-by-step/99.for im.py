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

# # 14696 딱지놀이 ## 
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

# # 2628 종이 자르기 ### 

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


# # 1244 스위치 켜고 끄기

# N = int(input())
# switch = [99] + list(map(int, input().split()))
# # print(switch)
# st_num = int(input())
# for _ in range(st_num):
#     gen, num = map(int, input().split())
#     # 남
#     if gen == 1:
#         for i in range(1, len(switch)):
#             if i % num == 0:
#                 if switch[i] == 1:
#                     switch[i] = 0
#                 else:
#                     switch[i] = 1
#     # 여
#     elif gen == 2:
#         for i in range(1, len(switch)):
#             if i == num:
#                 if switch[i] == 1:
#                     switch[i] = 0
#                 else:
#                     switch[i] = 1
#                 for j in range(1, len(switch)):
#                     if 0<= i-j and i+j< len(switch):
#                         if switch[i-j] == switch[i+j]:
#                             switch[i-j] = 1 - switch[i-j]
#                             switch[i+j] = 1 - switch[i+j]
#                         else:
#                             break
        

# for i in range(1, N+1):
#     print(switch[i], end =' ')
#     if i % 20 == 0:
#         print()




# # 2477 참외밭
# fruit = int(input())
# direction = [[] for _ in range(4)]
# for i in range(6):
#     di, length = map(int, input().split())
#     if di ==1:
#         direction[0].append(length)
#     elif di ==2:
#         direction[1].append(length)
#     elif di ==3:
#         direction[2].append(length)
#     else:
#         direction[3].append(length)
# print(direction)

# big = []
# small = []

# for i in direction:
#     if len(i) == 1:
#         a = i.pop()
#         big.append(a)
#     else:
#         small.append(min(i))

# # print(big, small)

# result = (big[0] * big[1] * fruit) - (small[0]*small[1]*fruit)
# print(result)

# # 2477 참외밭
# fruit = int(input())
# direction = []
# length = []
# row = []
# col = []

# for i in range(6):
#     dir, leng = map(int, input().split())
#     direction.append(dir)
#     length.append(leng)
#     if dir == 1 or dir == 2:
#         row.append(leng)
#     else:
#         col.append(leng)

# # print(direction, length)
# s1 = 0
# s2 = 0
# for j in range(5):
#     if direction[j] == 4 and direction[j+1] == 1:
#         s1 = j
#         s2 = j+1
#         break
#     if direction[j] == 3 and direction[j+1] == 2:
#         s1 = j
#         s2 = j+1
#         break
#     if direction[j] == 2 and direction[j+1] == 4:
#         s1 = j
#         s2 = j+1
#         break
#     if direction[j] == 1 and direction[j+1] == 3:
#         s1 = j
#         s2 = j+1
#         break
# if (direction[0]==1 and direction[-1] == 4):
#     s1 = 0
#     s2 = 5
# if (direction[0]==2 and direction[-1] == 3):
#     s1 = 0
#     s2 = 5
# if (direction[0]==4 and direction[-1] == 2):
#     s1 = 0
#     s2 = 5
# if (direction[0]==3 and direction[-1] == 1):
#     s1 = 0
#     s2 = 5


# small = length[s1] * length[s2] * fruit
# big = max(row) * max(col) * fruit
# result = big - small
# print(result)
    

# # print(s1, s2)
# # 가장 큰 사각형의 넓이


# # 10157 자리배전
# col, row = map(int, input().split())
# arr = [[[] for _ in range(col)] for _ in range(row)]
# for i in range(row):
#     for j in range(col):
#         arr[row - i - 1][j] = [j+1, i+1]
# # pprint(arr)
# K = int(input())
# # 상 우 좌 하
# # print(visited)

# di = [-1, 0, 0, 1]
# dj = [0, 1, -1, 0]

# k = 0
# cnt = 0
# ni = row - 1
# nj = 0
# r_i = 0
# r_j = 0

# visited = [[0 for _ in range(col)] for _ in range(row)]

# for i in range(row):
#     for j in range(col):
#         visited[ni][nj] = 1
#         cnt += 1
#         if cnt >= K:
#             r_i = ni
#             r_j = nj
#             break
#         newi = ni + di[k]
#         newj = nj + dj[k]
#         for _ in range(4):
#             if newi < 0 or newi >= row or newj < 0 or newj >= col or visited[newi][newj] !=0:
#                 k+=1
#                 if k == 4:
#                     k = 0
#                 newi = ni + di[k]
#                 newj = nj + dj[k]
#         ni = newi
#         nj = newj

# result = arr[r_i][r_j]
# # pprint(visited)
# # print(cnt)
# # print(K)

# pos = True

# if K > col * row:
#     pos = False

# if pos == False:
#     print(0)
# else:
#     print(*result)




# # 10158 개미
# # 오위 좌위 좌하 우위
# di = [-1, -1, 1, 1]
# dj = [1, -1, -1, 1]
# def right_up(i, j, cnt):
#     if cnt == move:
#         return i, j, cnt

#     if i == row  and j == col:
#         return left_down(i-1, j-1, cnt)
    
#     if i == row and j < col:
#         return left_down(i-1, j, cnt)
    
#     if i < row and j == col:
#         return left_up(i, j-1, cnt)
#     print(0)
#     cnt += 1
#     i -= 1
#     j += 1
#     return right_up(i, j, cnt)
    

# def left_up(i, j, cnt):
#     if cnt == move:
#         return i, j, cnt
    
#     if i == row  and j == col:
#         return right_down(i-1, j-1, cnt)
    
#     if i == row and j < col:
#         return left_down(i-1, j, cnt)
    
#     if i < row and j == 0:
#         return right_up(i, j, cnt)
#     print(1)
#     cnt += 1
#     i -= 1
#     j -= 1
#     return left_up(i, j, cnt)


# def left_down(i, j, cnt):
#     if cnt == move:
#         return i, j, cnt
    
#     if i == 0  and j == 0:
#         return right_up(i, j, cnt)
    
#     if i == 0 and j > 0:
#         return left_up(i, j, cnt)
    
#     if i > 0 and j == 0:
#         return right_down(i, j, cnt)
#     print(2)
#     cnt += 1
#     i += 1
#     j -= 1
#     return left_down(i, j, cnt)

# def right_down(i, j, cnt):
#     if cnt == move:
#         return i, j, cnt
    
#     if i == 0  and j == col:
#         return left_up(i, j, cnt)
    
#     if i == 0 and j < col:
#         return right_up(i, j, cnt)
    
#     if i > 0 and j == col:
#         return left_down(i, j, cnt)
#     print(3)
#     cnt += 1
#     i += 1
#     j += 1
#     return right_down(i, j, cnt)


# col, row = map(int, input().split())
# s_j, s_i = map(int, input().split())
# move = int(input())
# arr = [[0 for _ in range(col)] for _ in range(row)]
# start_i = row - s_i-1
# start_j = s_j
# cnt_v = 0
# result = right_up(start_i, start_j, cnt_v)
# print(result)

# # pprint(arr)


# # 10158 개미
# import sys
# sys.setrecursionlimit(100000)
# def right_up(i, j, cnt):
#     if cnt == move:
#         return i, j, cnt

#     if i == row  and j == col:
#         return left_down(i, j, cnt)
    
#     elif i == row and j < col:
#         return right_down(i, j, cnt)
    
#     elif 0 < i < row and j == col:
#         return left_up(i, j, cnt)
#     cnt += 1
#     i += 1
#     j += 1
#     # print(0) 
#     # print(i, j, cnt)
#     return right_up(i, j, cnt)
    

# def left_up(i, j, cnt):
#     if cnt == move:
#         return i, j, cnt

#     if i == row  and 0 < j < col:
#         return left_down(i, j, cnt)
    
#     elif i == row and j ==0:
#         return right_down(i, j, cnt)
    
#     elif i < row and j == 0:
#         return right_up(i, j, cnt)
#     cnt += 1
#     i += 1
#     j -= 1
#     # print(1)
#     # print(i, j, cnt)
#     return left_up(i, j, cnt)

# def left_down(i, j, cnt):
#     if cnt == move:
#         return i, j, cnt

#     if i == 0  and 0 < j < col:
#         return left_up(i, j, cnt)
    
#     elif i == 0 and j == 0:
#         return right_up(i, j, cnt)
    
#     elif 0 < i < row and j == 0:
#         return right_down(i, j, cnt)
#     cnt += 1
#     i -= 1
#     j -= 1
#     # print(3)
#     # print(i, j, cnt)
#     return left_down(i, j, cnt)

# def right_down(i, j, cnt):
#     if cnt == move:
#         return i, j, cnt

#     if 0 < i < row  and j == col:
#         return left_down(i, j, cnt)
    
#     elif i == 0 and j == col:
#         return left_up(i, j, cnt)
    
#     elif i == 0 and 0 < j < col:
#         return right_up(i, j, cnt)
#     cnt += 1
#     i -= 1
#     j += 1
#     # print(4)
#     # print(i, j, cnt)
#     return right_down(i, j, cnt)


# col, row = map(int, input().split())
# s_j, s_i = map(int, input().split())
# move = int(input())
# # arr = [[0 for _ in range(col)] for _ in range(row)]
# cnt_v = 0
# result = right_up(s_i, s_j, cnt_v)
# # print(result)
# end_i = result[1]
# end_j = result[0]
# print(end_i, end_j)
# # pprint(arr)