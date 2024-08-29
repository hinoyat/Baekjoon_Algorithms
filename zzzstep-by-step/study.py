from pprint import pprint

# #2669 직사각형 네개의 합집합의 면적 구하기

# # 면적의 최대

# arr_len = 100
# arr = [[0 for _ in range(arr_len)]for _ in range(arr_len)]

# # 정수를 몇 번 입력하는지
# test = 4

# # test 동안 사각형 입력
# for tc in range(test):
#     co_lst = list(map(int,input().split()))
#     # [x1, y1, x2, y2]
#     # [1 , 2 , 3 , 4 ]
    
#     for i in range(co_lst[0], co_lst[2]):
#         for j in range(co_lst[1], co_lst[3]):
#             arr[j][i] = 1
#     # print(co_lst)
#     # co_lst.clear()  필요할 줄 알았는데 for문 돌 때마다 갱신되는 것을 알았습니다.

# # pprint(arr)

# # 면적의 합
# sum = 0

# # 2차원 배의 행을 하나씩 뜯어서
# for s in arr:
#     #하나씩 1인지 더했어요!
#     for i in range(arr_len):
#         if s[i] == 1:
#             sum += 1

# print(sum)


# # 종이 자르기
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


# # 23881 선택정렬 1
# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# lst = list(map(int, input().split()))

# # 몇 번 정렬 했는지
# cnt = 0
# # 횟수 채웠나요?
# end = False
# for i in range(len(lst)-1, -1, -1):
#     # 초기 변수
#     max_v = -0xffffff
#     max_idx = -1
#     # 최댓값 찾기
#     for j in range(i+1):
#         if lst[j] > max_v:
#             max_v = lst[j]
#             max_idx = j
#     # 마지막 인덱스가 최대가 아니면 자리 바꿔주기
#     if lst[i] != max_v:
#         lst[i], lst[max_idx] = lst[max_idx], lst[i]
#         cnt +=1
#     else:
#         pass
#     # 지정 횟수만큼 정렬 해줬으면 종료하고 값 프린뜨 하고횟수 채웠다고 해주기
#     if cnt == K:
#         print(lst[max_idx], lst[i])
#         end = True
#         break
#     # 왜 했는지 모르겠군요
#     max_v = -0xffffff

# # 횟수 미달이면 -1 출력
# if end == False:
#     print(-1)



# # 1654 랜선 자르기
# def check(lst):
#     start = 1
#     end = max(lst)
#     result = 0
#     while start<= end:
#         mid = (start+end)//2

#         cable = 0

#         for c in lst:
#             cable += c//mid
        
#         if cable < N:
#             end = mid - 1 
#         else:
#             result = mid
#             start = mid + 1
        
#     return result
    

# K, N = map(int,input().split())
# lst = [int(input()) for _ in range(K)]
# print(check(lst))


# # 2468 안전 영역
# from collections import deque

# def Rain(max_rain):
#     end = max_rain
#     max_v = 0
#     start_rain = 0
#     while start_rain < end:
#         visited = [[0] * N for _ in range(N)]
#         safe = 0
#         que = deque()
#         for i in range(N):
#             for j in range(N):
#                 if arr[i][j] > start_rain and visited[i][j]==0:
#                     que.append([i,j])
#                     safe += 1
                
#                 while que:
#                     qi, qj = que.popleft()
#                     for pi, pj in [[0,1],[1,0],[0,-1],[-1,0]]:
#                         ni = qi + pi
#                         nj = qj + pj
#                         if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0 and arr[ni][nj] > start_rain:
#                             visited[ni][nj] = 1
#                             que.append([ni,nj])
#         start_rain += 1
#         if safe > max_v:
#             max_v = safe

#     return max_v

# N = int(input())
# arr = [list(map(int, input().split()))for _ in range(N)]

# max_rain = 0
# for i in arr:
#     if max(i) > max_rain:
#         max_rain = max(i)


# print(Rain(max_rain))