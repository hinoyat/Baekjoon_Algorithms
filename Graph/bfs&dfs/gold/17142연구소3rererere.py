#
#
#
#
#
#
# # 방법 1
# '''
# 구역을 찾아서 구역 번호대로 매겨놓고 그 번호에 있는 바이러스 포인트를 찾는다
# 그 머냐 찾은 구역보다 바이러스 설치 포인트가 적으면 그 머냐 -1
# 1번 2번 3번 이케 있으면 1번 하나 2번 하나 3번 하나 뽑는다
# '''
# from pprint import pprint
#
# # 안녕
# '''
# 구역마다 하나씩 어케 뽑아???????????????????????????????????
# 이 딕셔너리에서 하나씩 뽑아야 하는디 어케 뽑아?????????????????????????????
# ?????????????????????????????????????????????????????????????????
# ??????????????????????????????????????????????????????????????
# '''
# from collections import deque, defaultdict
#
#
# def BFS(si, sj):
#     que = deque()
#     que.append((si, sj))
#     area[si][sj] = 1
#     while que:
#         qi, qj = que.popleft()
#         if arr[qi][qj] == 2:
#             dct[area_num].append((qi, qj))
#         for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#             ni, nj = qi + di, qj + dj
#             if ni < 0 or nj < 0 or ni >= N or nj >= N or arr[ni][nj] == 1 or area[ni][nj] == 1: continue
#             que.append((ni, nj))
#             area[ni][nj] = 1
#
# def supernova(lst):
#     visited = [[0] * N for _ in range(N)]
#     sque = deque()
#     time = 0
#     for si, sj in lst:
#         visited[si][sj] = 1
#         sque.append((si, sj))
#     while sque:
#         qi, qj = sque.popleft()
#         for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#             ni, nj = qi + di, qj + dj
#             if ni < 0 or nj < 0 or ni >= N or nj >= N or arr[ni][nj] == 1 or visited[ni][nj] != 0: continue
#             sque.append((ni, nj))
#             visited[ni][nj] = visited[qi][qj] + 1
#             time = max(time, visited[ni][nj])
#     # pprint(visited)
#     # print(time)
#     return time
#
# def comb(cnt, lst):
#     global ans
#     if cnt == area_num:
#         result = supernova(lst)
#         ans = min(ans, result)
#         # print(lst)
#         return
#
#     for si, sj in dct[cnt]:
#         comb(cnt + 1, lst + [(si, sj)])
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split()))for _ in range(N)]
#
# area = [[0] * N for _ in range(N)]
# area_num = 0
# dct = defaultdict(list)
# ans = 9999
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 2 and area[i][j] == 0:
#             BFS(i, j)
#             area_num += 1
#
#
# comb(0, [])
#
# # print(ans)
#
# # print(area_num)
# print(dct)


#
# # 연구소 3
# from collections import deque
# from pprint import pprint
# import sys
# input = sys.stdin.readline
#
# def com(idx, cnt):
#     global ans
#     if cnt == M:
#         que = deque()
#         for i in range(virus_cnt):
#             if virus_com[i] == 1:
#                 que.append(virus[i])
#         result = test(que)
#         ans = min(result, ans)
#         return
#
#     for i in range(idx, virus_cnt):
#         virus_com[i] = 1
#         com(i+1, cnt + 1)
#         virus_com[i] = 0
#
#
# def test(que):
#     time = 0
#     # 방문하기
#     experiment = [[-1] * N for _ in range(N)]
#     for si, sj in que:
#         experiment[si][sj] = 0
#     # print(que)
#     # print(experiment)
#     while que:
#         qi, qj = que.popleft()
#         for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
#             ni, nj = qi + di, qj + dj
#             if ni < 0 or nj < 0 or ni >= N or nj >= N or experiment[ni][nj] != -1: continue
#             if arr[ni][nj] == 2:
#                 experiment[ni][nj] = experiment[qi][qj] + 1
#                 que.append((ni,nj))
#             elif arr[ni][nj] == 0:
#                 experiment[ni][nj] = experiment[qi][qj] + 1
#                 time = max(time, experiment[ni][nj])
#                 que.append((ni,nj))
#
#     for i in range(N):
#         for j in range(N):
#             # if experiment[i][j] == -1 and arr[i][j] == 2:
#             #     return 10000
#             if experiment[i][j] == -1 and arr[i][j] == 0:
#                 return 10000
#
#     return time
#
#
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split()))for _ in range(N)]
#
# ans = 1000
# virus = []
# # 퍼질 수 있는 곳 뽑아서 넣고 조합 돌리기?
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 2:
#             virus.append((i, j))
# virus_cnt = len(virus)
# virus_com = [0] * virus_cnt
# # pprint(experiment)
# com(0, 0)
# if ans == 1000:
#     print(-1)
# else:
#     print(ans)

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n, m = map(int, input().split())
array = []

INF = int(1e9)
answer = INF # 총 소요 시간
wall = 0 # 벽의 개수
virus_pos = [] # 2 번 좌표값
empty = 0 # 빈칸
for i in range(n):
    data = list(map(int, input().split()))
    array.append(data)
    for j in range(n):
        if data[j] == 2:
            virus_pos.append((i, j))
        elif data[j] == 1:
            wall += 1
        else:
            empty += 1
if empty == 0:
    print(0)
    exit(0)

def bfs(v_list):
    visited = [[-1] * n for _ in range(n)]
    queue = deque([])
    for i in range(m):
        queue.append([v_list[i][0], v_list[i][1]])
        visited[v_list[i][0]][v_list[i][1]] = 0
    time = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1: # not visited
                if array[nx][ny] == 0: # 빈칸
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])
                    time = max(time, visited[nx][ny])
                elif array[nx][ny] == 2: # virus
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny])

    # check
    check = 0
    for i in range(n):
        check += visited[i].count(-1)
    if check == wall:
        return time
    else:
        return INF

for comb in combinations(virus_pos, m):
    answer = min(bfs(comb), answer)

if answer != INF:
    print(answer)
else:
    print(-1)
