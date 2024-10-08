# '''
# ## 2
# 4 11
# ..XXX...X..
# .X.XXX...L.
# ....XXX..X.
# X.L..XXX...
#
# ## 3
# 10 2
# .L
# ..
# XX
# XX
# XX
# XX
# XX
# XX
# ..
# .L
#
# ## 2
# 8 17
# ...XXXXXX..XX.XXX
# ....XXXXXXXXX.XXX
# ...XXXXXXXXXXXX..
# ..XXXXX.LXXXXXX..
# .XXXXXX..XXXXXX..
# XXXXXXX...XXXX...
# ..XXXXX...XXX....
# ....XXXXX.XXXL...
# '''
#
# def removeice(que):
#     global ice
#     new_que = que
#     check = set()
#     while que:
#         qi, qj = que.popleft()
#         for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
#             ni, nj = qi + di, qj + dj
#             if ni < 0 or nj < 0 or ni >= R or nj >= C or arr[ni][nj] == '.' or arr[ni][nj] == 'L' : continue
#             # ice.add((ni, nj))
#             if (ni, nj) in check:continue
#             if arr[ni][nj] == 'X':
#                 if (ni, nj) in ice:
#                     new_que.append((ni, nj))
#                 else:
#                     check.add((ni, nj))
#             print(check)
#             print(new_que)
#     for i in list(check):
#         ice.add(i)
#     print(check)
#     return new_que
#
# def move(bird):
#     bi1, bj1 = bird[0][0], bird[0][1]
#     bi2, bj2 = bird[1][0], bird[1][1]
#     visited = [[0] * C for _ in range(R)]
#     check_que = deque()
#     flag = False
#     check_que.append((bi1, bj1))
#     visited[bi1][bj1] = 1
#     while check_que:
#         qi, qj = check_que.popleft()
#         if (qi, qj) == (bi2, bj2):
#             flag = True
#             break
#         for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
#             ni, nj = qi + di, qj + dj
#             if ni < 0 or nj < 0 or ni >= R or nj >= C or visited[ni][nj]: continue
#             if arr[ni][nj] == 'X':
#                 if (ni, nj) in ice:
#                     check_que.append((ni, nj))
#                     visited[ni][nj] = 1
#             else:
#                 check_que.append((ni, nj))
#                 visited[ni][nj] = 1
#         print(check_que)
#
#     return flag
#
# def solve(time, que, bird):
#
#     new_que = que
#     while True:
#         if move(bird):
#             return time
#         # 얼음 지워주기
#         time += 1
#         new_que = removeice(que)
#         print(2)
#
#
#     return time
#
#
#
# # 백조의 호수
# from pprint import pprint
# from collections import deque
# R, C = map(int, input().split())
# arr = [list(input()) for _ in range(R)]
# pprint(arr)
# # 물 공간은 . or L
# # 필요한 작업
# # 시간 체크 함수 한 번 돌 때 마 따 시 간 1 씩 증 가
# # 얼음의 좌표 담기 set BFS에서 만날 때 remove 해주기
# ice = set()
#
# bird = []
#
# for i in range(R):
#     for j in range(C):
#         if arr[i][j] == '.' or arr[i][j] == 'L':
#             for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
#                 ni, nj = i + di, j + dj
#                 if ni < 0 or nj < 0 or ni >= R or nj >= C or arr[ni][nj] == '.' or arr[ni][nj] == 'L' or (ni, nj) in ice:continue
#                 ice.add((ni, nj))
#         if arr[i][j] == 'L':
#             bird.append((i, j))
#
#
#
# first_que = deque(list(ice))
# print(solve(0, first_que, bird))








'''
## 2
4 11
..XXX...X..
.X.XXX...L.
....XXX..X.
X.L..XXX...

## 3
10 2
.L
..
XX
XX
XX
XX
XX
XX
..
.L

## 2
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
'''


def moving(water, bird):
    new_water = deque()
    si, sj = bird[0][0], bird[0][1]
    ei, ej = bird[1][0], bird[1][1]
    while water:
        qi, qj = water.popleft()
        if (qi, qj) == (ei, ej):
            return True, water
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if ni < 0 or nj < 0 or ni >= R or nj >= C or bird_visited[ni][nj]: continue
            if arr[ni][nj] == 'X':
                new_water.append((ni, nj))
                bird_visited[ni][nj] = 1
            else:
                water.append((ni, nj))
                bird_visited[ni][nj] = 1

    return False, new_water

def removeice(que):
    visited = [[0] * C for _ in range(R)]
    new_que = deque()
    while que:
        qi, qj = que.popleft()
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if ni < 0 or nj < 0 or ni >= R or nj >= C or visited[ni][nj]: continue
            if arr[ni][nj] == 'X':
                new_que.append((ni, nj))
                visited[ni][nj] = 1
                arr[ni][nj] = '.'
    return new_que

# 백조의 호수
from pprint import pprint
from collections import deque
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
# 물 공간은 . or L
# 필요한 작업
# 시간 체크 함수 한 번 돌 때 마 따 시 간 1 씩 증 가
# que 여러개 호ㅓㅏㄹ용

water = deque()

bird = []

for i in range(R):
    for j in range(C):
        if arr[i][j] == '.' or arr[i][j] == 'L':
            water.append((i, j))
        if arr[i][j] == 'L':
            bird.append((i, j))

bird_visited = [[0] * C for _ in range(R)]
ans = 0
result = False

start_move = deque()
start_move.append((bird[0][0], bird[0][1]))
bird_visited[bird[0][0]][bird[0][1]] = 1
while not result:
    result, move = moving(start_move, bird)
    water = removeice(water)
    start_move = move
    ans += 1
print(ans - 1)
