# N = int(input())
# data = [list(input()) for _ in range(N)]
# cnt_lst = []
# d = 0
#
# for r in range(N):
#     for c in range(N):
#         if data[r][c] == '1':
#             data[r][c] = 1
#             q = []
#             q.append([r, c])
#             cnt = 1
#             d += 1
#
#             while q:
#                 r, c = q.pop()
#                 for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#                     if 0 <= r+dr < N and 0 <= c+dc < N and data[r+dr][c+dc] == '1':
#                         q.append([r+dr, c+dc])
#                         data[r+dr][c+dc] = 1
#                         cnt += 1
#             cnt_lst.append(cnt)
#
# cnt_lst.sort()
#
# print(d)
# for n in cnt_lst:
#     print(n)


# test_case = 10
# for tc in range(1, test_case + 1):
#     N = int(input())
#     buil = list(map(int, input().split()))
#     sun = 0
#     for s in range(2, N - 2):
#         b_lst = sorted(buil[s - 2:s + 3])
#         print(b_lst)
#         if buil[s] > b_lst[3]:
#             sun += buil[s] - b_lst[3]
#     # print(f'#{tc} {sun}')



# T = int(input())
# for tc in range(1, T+1):

#     front_card = []     # 앞쪽 카드 리스트
#     back_card = []      # 뒤쪽 카드 리스트

#     N = int(input())        # 카드 수
#     cards = input().split()  # 카드 리스트

#     if N % 2 == 0: # 카드 개수 짝수
#         for idx in range(N):
#             if idx < int(N/2):
#                 front_card.append(cards[idx])
#             else:
#                 back_card.append(cards[idx])

#     else:          # 카드 개수 홀수
#         for idx in range(N):
#             if idx <= int(N/2): 
#                 front_card.append(cards[idx])
#             else:
#                 back_card.append(cards[idx])


#     print(f"#{tc}", end=' ')
#     for i in range(len(back_card)): # 앞쪽 카드 리스트, 뒤쪽 카드리스트 하나씩 출력
#         print(front_card[i], end=' ')
#         print(back_card[i], end=' ')
#     if len(front_card) != len(back_card): # 홀수개라면 앞쪽 카드 리스트 남은 한장 마져 출력
#         print(front_card[-1], end=' ')

#     print()


# # 15686. 치킨 배달
# N, M = map(int, input().split())
# city = [[-1] * (N+1)] + [[-1] + list(map(int, input().split())) for _ in range(N)]
#
# chicken = []
# home = []
# for i in range(N+1):
#     for j in range(N+1):
#         if city[i][j] == 1:
#             home.append([i, j])
#         if city[i][j] == 2:
#             chicken.append([i, j])
#
#
# cn = len(chicken)
# MinV = 10e5
# for i in range(1 << cn):
#     subset = []
#     for j in range(cn):
#         if i & (1 << j):
#             subset.append(chicken[j])
#
#     chicken_dist = 0
#     if len(subset) == M:
#         # print(subset)
#         for h in home:
#             MinS = 10e5
#             for c in subset:
#                 store_dist = abs(h[0] - c[0]) + abs(h[1] - c[1])
#                 if MinS > store_dist:
#                     MinS = store_dist
#             # print(MinS)
#             chicken_dist += MinS
#             # print(chicken_dist)
#
#
#         if MinV > chicken_dist:
#             MinV = chicken_dist
#
# print(MinV)

# import sys
# input = sys.stdin.readline
# from collections import deque
# def supernova(start, end):
#     que = deque([(start, 0)])
#     check = set()
#     check.add(start)
#     ans = 100000000000
#     while que:
#         now, cnt = que.popleft()
#         if now == end:
#             ans = min(ans, cnt)
#             return ans
#
#         for newval in (now * 2, now - 1, now + 1):
#             if newval <= 100000 and newval not in check:
#                 if newval == now * 2:
#                     que.append((newval, cnt))
#                 else:
#                     que.append((newval, cnt+1))
#                 check.add(newval)
#
#     return ans
#
# N, K = map(int, input().split())
# print(supernova(N, K))


# def Джедайские(che):
#     global ans
#     result = int(che[0])
#
#     for i in range(len(che)):
#         if che[i] == '+':
#             result += int(che[i + 1])
#         elif che[i] == '-':
#             result -= int(che[i + 1])
#
#     ans = max(ans, result)
#
#
# lst = list(input())
# ans = 0
# # print(lst)
#
# num = []
# order = []
#
# idx = 0
# numv = ''
# while idx < len(lst):
#     if lst[idx] == '+' or lst[idx] == '-':
#         num.append(numv)
#         num.append(lst[idx])
#         numv = ''
#     else:
#         numv += lst[idx]
#     idx += 1
#
#     if idx == len(lst):
#         num.append(numv)
# # print(num, order)
# import copy
# # 연산자 기준으로 양 옆 묶어서 보내기
# check = []
# for i in range(len(num)):
#     if num[i] == '+' or num[i] == '-':
#         check = copy.deepcopy(num)
#         new_num = check[i - 1] + check[i + 1]
#         check[i] = new_num
#         check.pop(i + 1)
#         check.pop(i - 1)
#         Джедайские(check)
#         # print(check)
#
# print(ans)

# 17472. 다리 만들기 2
from collections import deque, defaultdict

# 섬 찾는 함수
def FindIsland():
    global num
    q = deque()
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 1이고 방문한 적 없는 곳에서 시작
            if arr[i][j] == 1 and visited[i][j] == 0:
                num += 1
                arr[i][j] = num
                q.append((i, j))
                visited[i][j] = 1
                island[num].append((i, j))

            while q:
                i, j = q.popleft()
                for di, dj in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                        arr[ni][nj] = num  # 섬 번호 부여
                        q.append((ni, nj))
                        visited[ni][nj] = 1
                        island[num].append((ni, nj))


# 다리 건설하는 함수
def Bridge():
    edges = set()
    for k, v in island.items():
        for i, j in v:
            for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
                nr, nc = i + dr, j + dc
                length = 0
                while 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != k:
                    if arr[nr][nc] > k:
                        if length >= 2:
                            edges.add((k, arr[nr][nc], length))
                        break
                    length += 1
                    nr, nc = nr + dr, nc + dc

    return list(edges)


def Find(x):
    if x != p[x]:
        p[x] = Find(p[x])
    return p[x]


def Union(x, y):
    px = Find(x)
    py = Find(y)

    if px != py:
        if rank[px] < rank[py]:
            p[px] = py
        elif rank[px] > rank[py]:
            p[py] = px
        else:
            p[px] = py
            rank[py] += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

num = 0  # 섬 개수
island = defaultdict(list)
FindIsland()
edges = Bridge()
pp(arr)
edges.sort(key=lambda x: x[2])

p = [i for i in range(num + 1)]
rank = [0] * (num + 1)
ans = 0
cnt = 0
for s, e, w in edges:
    if Find(s) != Find(e):
        Union(s, e)
        ans += w
        cnt += 1

# 섬이 모두 연결되었는지 확인 => 간선 수 == 노드 수 - 1
if cnt == num - 1:
    print(ans)
else:
    print(-1)