# 마법사 상어와 비바라기
from pprint import pprint as ppp
N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]

info = [list(map(int, input().split())) for _ in range(M)]

# 1번과 N번 연결 N되면 0, 0< 면 N-1 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
# 음수 되면 걍 N 더해주면 댐
moving = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}

# 이동후 일단 해당 칸에 물 내려
# 이동 후 대각선 4방향 물이 있으면 한 칸당 1 +

# 그리고 나머지 칸에 2 이상이면 1씩 추가

cnt = 0
ans = 0
point = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
while cnt <= M:
    # 어디로 가는지
    movei, movej = moving[info[cnt][0]]
    movecnt = info[cnt][1]

    check = set()

    cross = []

    # 이동하기 여기서 다 바꾸고 다음에 체크
    # 비 내리기
    while point:
        mi, mj = point.pop()
        mi += movei * movecnt
        mj += movej * movecnt
        if mi < 0:
            while True:
                mi += N
                if mi >= 0:
                    break
        if mj < 0:
            while mj < 0:
                mj += N
                if mj >= 0:
                    break
        if mi >=N:
            mi %= N

        if mj >= N:
            mj %= N

        arr[mi][mj] += 1
        check.add((mi, mj))
        cross.append((mi, mj))


    for mi, mj in cross:
        for s in (2, 4, 6, 8):
            di, dj = moving[s]

            ni, nj = mi + di, mj + dj
            if 0<= ni < N and 0<= nj < N:
                if arr[ni][nj] > 0:
                    arr[mi][mj] += 1

    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in check:
                point.append((i, j))
                arr[i][j] -= 2
    # ppp(arr)
    # print(len(point))
    cnt += 1
    if cnt == M:
        break
# print(arr)

for j in arr:
    ans += sum(j)
print(ans)
