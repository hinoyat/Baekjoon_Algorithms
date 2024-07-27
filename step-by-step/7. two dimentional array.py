# # 2738 행렬 덧셈 # # 백준 제출했던 부분 보고 뭐때매 틀렸었는지 알아내라

# n, m = map(int,input().split())

# n개의 행 m개의 열
# array_a = [[0 for _ in range(m)] for _ in range(n)]
# array_b = [[0 for _ in range(m)] for _ in range(n)]
# print(array_a)
# print(array_b)


# for i in range(n):
#     array_a[i] = list(map(int, input().split()))

# for d in range(n):
#     array_b[d] = list(map(int, input().split()))

# print(array_a)
# print(array_b)


# sum_array = [[0 for _ in range(m)] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         sum_array[i][j] = int(array_a[i][j]) + int(array_b[i][j])


# for num in range(n):
#     for num1 in range(m):
#         print(sum_array[num][num1], end=" ")
#     print()


# # 2566 최댓값
# array_len = 9

# arr = [[0 for _ in range(array_len)] for _ in range(array_len)]
# # print(arr)
# arr_lst = []

# for i in range(array_len):
#     num = list(map(int,input().split()))
#     for s in range(array_len):
#         arr[i][s] = num[s]

# # print(arr)


# arr_idx = [0, 0]


# arr_max = 0
# for i in range(array_len):
#     for s in range(array_len):
#         if arr[i][s] >= arr_max:
#             arr_max = arr[i][s]
#             arr_idx[0] = i+1
#             arr_idx[1] = s+1

# print(arr_max)
# print(*arr_idx)


# # 10798 세로 읽기 틀린 것
# array_len = 15
# arr = [['*' for _ in range(array_len)] for _ in range(array_len)]
# # print(arr)
# sorted_lst = []
# for i in range(5):
#     string = input()
#     for s in  range(len(string)):
#         arr[i][s] = string[s]
# print(arr)

# for i in range(len(string)):
#     for s in range(len(string)):
#         sorted_lst.append(arr[s][i])

# print(sorted_lst)
# for i in sorted_lst:
#     if i != '*':
#         print(i,end='')
# print()


# # 10798 세로 읽기 2

# arr = [['*' for _ in range(15)] for _ in range(15)]
# # print(arr)

# arr_lst = []
# for i in range(5):
#     string = list(input())
#     for s in range(len(string)):
#         arr[i][s] = string[s]
# # print(arr)

# for i in range(15):
#     for s in range(15):
#         arr_lst.append(arr[s][i])

# # print(arr_lst,end='')

# for d in arr_lst:
#     if d != '*':
#         print(d,end='')
#     else:
#         pass



# # 2563 색종이

# arr = [['*' for _ in range(25)]for _ in range(17)]

# cnt_black = 0

# n = int(input())
# for i in range(n):
#     x, y = map(int,input().split())
#     for x_i in range(10):
#         for x_s in range(10):
#             arr[y+ x_i][x+x_s] = '1'


# for black in arr:
#     s = black.count('1')
#     cnt_black += s
# print(cnt_black)



# ## 22
# arr = [[0 for _ in range(100)]for _ in range(100)]


# n = int(input())
# for _ in range(n):
#     x, y = map(int,input().split()) # y 행 # x 열 
#     for x_i in range(10):
#         for y_i in range(10):
#             arr[x+x_i-1][y+ y_i-1] = 1

# cnt_black = 0
# for x in range(100):
#     for y in range(100):
#         if arr[x][y] != 1:
#             pass
#         else:
#             cnt_black +=1

# # for x in range(100):
# #     for y in range(100):
# #         cnt_black += arr[x][y]

# print(cnt_black)


