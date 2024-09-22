# 연구소 2
from collections import deque
from pprint import pprint
import sys
input = sys.stdin.readline

def com(idx, cnt):
    global ans
    if cnt == M:
        que = deque()
        for i in range(virus_cnt):
            if virus_com[i] == 1:
                que.append(virus[i])
        result = test(que)
        ans = min(result, ans)
        return

    for i in range(idx, virus_cnt):
        virus_com[i] = 1
        com(i+1, cnt + 1)
        virus_com[i] = 0


def test(que):
    time = 0
    # 방문하기
    experiment = [[-1] * N for _ in range(N)]
    for si, sj in que:
        experiment[si][sj] = 0
    # print(que)
    # print(experiment)
    while que:
        qi, qj = que.popleft()
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = qi + di, qj + dj
            if ni < 0 or nj < 0 or ni >= N or nj >= N or arr[ni][nj] == 1 or experiment[ni][nj] != -1: continue
            que.append((ni,nj))
            experiment[ni][nj] = experiment[qi][qj] + 1

    for i in range(N):
        for j in range(N):
            if experiment[i][j] == -1 and arr[i][j] == 2:
                return 10000
            elif experiment[i][j] == -1 and arr[i][j] == 0:
                return 10000
            else:
                time = max(time, experiment[i][j])
    # print(time)

    return time



N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]

ans = 1000
virus = []
# 퍼질 수 있는 곳 뽑아서 넣고 조합 돌리기?
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))
virus_cnt = len(virus)
virus_com = [0] * virus_cnt
# pprint(experiment)
com(0, 0)
if ans == 1000:
    print(-1)
else:
    print(ans)

