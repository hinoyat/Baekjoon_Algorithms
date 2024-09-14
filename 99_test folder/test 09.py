# import sys
#
# input = sys.stdin.readline
# N = int(input())
#
# lst = [list(map(int, input().split())) for _ in range(N)]
# lst.sort(key=lambda x:(x[1], x[0]))
# # print(lst)
#
#
# start_time = lst[0][1]
# ans = 1
# for i in range(1, N):
#     if lst[i][0] >= start_time:
#         start_time = lst[i][1]
#         ans += 1
#
# print(ans)
#
from os import lseek


#
# import sys
# input = sys.stdin.readline
# N, M = map(int, input().split())
# num = list(map(int, input().split()))
# new_lst = [0] * (N + 1)
#
# for i in range(1, N + 1):
#     new_lst[i] = new_lst[i - 1] + num[i - 1]
# # print(new_lst)
# for _ in range(M):
#     a, b = map(int, input().split())
#     print(new_lst[b] - new_lst[a - 1])


# import sys
# input = sys.stdin.readline

# def supernova(level, val):
#     global min_a, max_a
#
#     if level == N:
#         min_a = min(min_a, val)
#         max_a = max(max_a, val)
#         return
#
#     for i in range(4):
#         if order[i] > 0:
#             order[i] -= 1
#             if i == 0:
#                 supernova(level + 1, val + num_list[level])
#             elif i == 1:
#                 supernova(level + 1, val - num_list[level])
#             elif i == 2:
#                 supernova(level + 1, val * num_list[level])
#             else:
#                 supernova(level + 1, int(val / num_list[level]))
#             order[i] += 1
#
#
#
# N = int(input())
# num_list = list(map(int, input().split()))
# order = list(map(int, input().split()))
# min_a = 11e8
# max_a = -11e8
#
# supernova(1, num_list[0])
# print(max_a)
# print(min_a)

#
# import sys
# input = sys.stdin.readline
#
# N, M = map(int,input().split())
#
# tree = list(map(int, input().split()))
#
# # H를 지정해야 한다 강지민 바보네 ㅋㅋ 이거 안 보이지?
#
# # M 미터 만큼의 나무를 가져
# start = 0
# end = max(tree)
#
# ans = 0
#
# # 1 2 3 일때 N 3 M 1이면 바로 리턴인가? 아 최댓값이면
#
# while start <= end:
#     mid = (start + end)//2
#     cut_val = 0
#     for i in tree:
#         if i >= mid:
#             cut_val += i - mid
#     # 만이 잘라쑤면
#     if cut_val >= M:
#         start = mid + 1
#     # 조금 잘라쑤면
#     elif cut_val < M:
#         end = mid - 1
# print(end)



