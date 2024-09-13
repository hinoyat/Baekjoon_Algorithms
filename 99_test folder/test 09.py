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


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]
# print(lst)
idx = N - 1
ans = 0
while M > 0:
    if lst[idx] <= M:
        ans += M // lst[idx]
        # print(M, lst[idx])
        M %= lst[idx]

        # print(M)
    idx -= 1
    if idx == -1:
        break
print(ans)
