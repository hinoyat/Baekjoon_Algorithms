from collections import deque, defaultdict
import sys
input = sys.stdin.readline
def find(c):
    while parent[c] != c:
        c = parent[c]

    return c


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return

    if parent[a] > parent[b]:
        parent[a] = b
    else:
        parent[b] = a

def BFS(si, sj):
    global num
    que = deque()
    que.append((si, sj))
    # print(que)
    info[si][sj] = num
    land[num].append((si, sj))

    while que:
        qi, qj = que.popleft()
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if 0<= ni < N and 0<= nj < M and arr[ni][nj] == 1 and info[ni][nj] == 0:
                info[ni][nj] = num
                que.append((ni, nj))
                land[num].append((ni, nj))

def find_bridge(i, j):
    my_land = info[i][j]
    result = []
    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        other_land = 0
        bridge = 0
        ni = i + di
        nj = j + dj
        mid = 0
        if 0 > ni or 0 > nj or ni >= N or nj >= M:
            break
        while True:
            if 0 > ni or 0 > nj or ni >= N or nj >= M:
                break

            if info[ni][nj] != 0 and info[ni][nj] != my_land:
                if mid <= 1:
                    break
                bridge = mid
                other_land = info[ni][nj]
                result.append((bridge, my_land, other_land))
                break
            # 내 땅 만나면 X
            if info[ni][nj] == my_land:
                break
            mid += 1
            ni = ni + di
            nj = nj + dj
            # 다른 땅 만나면 O

    return result

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

info = [[0] * M for _ in range(N)]
num = 1
land = defaultdict(list)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not info[i][j]:
            BFS(i, j)
            num += 1

pos =[]
for i in range(1, num):
    for v in land[i]:
        # print(v[0], v[1])
        r = find_bridge(v[0], v[1])
        if r:
            for b in r:
                pos.append(b)

pos.sort()
parent = [i for i in range(num + 1)]
ans = 0
cnt = 0
for val, c1, c2 in pos:
    if find(c1) != find(c2):
        union(c1, c2)
        ans += val
        cnt += 1
# print(cnt, num)
if num - 2 == cnt:
    print(ans)
elif num - 2 != cnt or ans == 0:
    print(-1)
else:
    print(-1)