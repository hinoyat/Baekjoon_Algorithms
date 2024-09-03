import sys
input = sys.stdin.readline

def supernova(si, sj, sum_v):
    global min_v
    if sum_v > min_v:
        return
    if si == N-1 and sj == N-1:
        if sum_v < min_v:
            min_v = sum_v

    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        ni = si + di
        nj = sj + dj
        if ni < 0 or nj < 0 or ni >= N or nj >= N or visited[ni][nj]!= 0:
            continue
        else:
            visited[ni][nj] = 1
            supernova(ni, nj, sum_v + arr[ni][nj])
            visited[ni][nj] = 0


N = int(input())
cnt = 1
while N != 0:
    arr = [list(map(int, input().split()))for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    min_v = 21e8
    supernova(0, 0, arr[0][0])
    print(f'Problem {cnt}: {min_v}')
    N = int(input())
    cnt += 1