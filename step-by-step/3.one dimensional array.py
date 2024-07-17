# # 10807

# n = int(input())
# num_list = list(map(int,input().split()))
# v = int(input())

# s=0
# for i in range(len(num_list)):
#     if num_list[i] == v:
#         s += 1
# print(s)

# # 10871

# n, x = map(int,input().split())
# num_list = list(map(int,input().split()))
# small_list = []

# for i in range(n):
#     if num_list[i] < x:
#         small_list.append(num_list[i])
# print(*small_list)

# # 10818
# import sys
# input = sys.stdin.readline
# n = int(input())
# num_list = list(map(int,input().split()))
# print(f'{min(num_list)} {max(num_list)}')



# # 2562

# a = 0
# num_list = []

# while a < 9:
#     number = int(input())
#     num_list.append(number)
#     a += 1
# for i in range(len(num_list)):
#     if max(num_list) == num_list[i]:
#         print(max(num_list))
#         print(i+1)

