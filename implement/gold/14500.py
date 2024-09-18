import sys
input = sys.stdin.readline

def supernova(i, j, level, val):
    global ans
    if level == block:
        ans = max(val, ans)
        return
    # 가지치기
    # cut_val = 0
    # for di, dj in ((1, 0), (0, -1), (0, 1), (-1, 0)):
    #     ni, nj = i + di, j + dj
    #     if ni < 0 or nj < 0 or ni >= N or nj >= M or visited[ni][nj]:
    #         continue
    #     cut_val += arr[ni][nj]
    #
    # if cut_val <= ans:
    #     return

    for di, dj in ((1, 0), (0, -1), (0, 1), (-1, 0)):
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= N or nj >= M or visited[ni][nj]:
            continue

        visited[ni][nj] = 1
        supernova(ni, nj, level + 1, val + arr[ni][nj])
        visited[ni][nj] = 0

def armagetddon(level, i, j, val):
    global ans
    if level == block:
        ans = max(val, ans)
        return

    for di, dj in ((1, 0), (0, -1), (0, 1), (-1, 0)):
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= N or nj >= M or visited[ni][nj]:
            continue
        visited[ni][nj] = 1
        armagetddon(level + 1, i, j, val + arr[ni][nj])
        visited[ni][nj] = 0


N, M = map(int, input().split())
block = 4
arr = []
min_v = 21e8
for i in range(N):
    lst = list(map(int, input().split()))
    min_v = min(min(lst), min_v)
    arr.append(lst)


visited = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        supernova(i, j, 1, arr[i][j])
        armagetddon(1, i, j, arr[i][j])
        visited[i][j] = 0

print(ans)