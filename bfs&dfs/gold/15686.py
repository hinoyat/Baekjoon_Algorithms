from pprint import pprint as p
from itertools import combinations
# 치킨배달
N, M = map(int, input().split())

arr = [list(map(int, input().split()))for _ in range(N)]
# p(arr)

# 집의 인덱스 구하기
home = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append([i,j])

# 치킨집의 인덱스
chi = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chi.append([i,j])
# print(home)
# print(chi)
min_v = 0xffffffff
# 조합 뽑기
for c in list(combinations(chi, M)):
    city = 0
    # 집 뽑기
    for h in home:
        sum_v = 21e8
        # 각 집집 마다의 최솟 값 찾기
        for j in c:
            sum_v2 = abs(j[0] - h[0]) + abs(j[1] - h[1])
            if sum_v2 < sum_v:
                sum_v = sum_v2
        city += sum_v
    if city < min_v:
        min_v = city

print(min_v)