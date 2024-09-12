# 구슬탈출

# 델타 구슬 동시에 움직임

# 파란 구슬 빠지면 return

# 구슬 움직임

# 최소 횟수 10 번 이상이면 - 1 못 빼도 -1

def move():

    # RED
    # BLUE
    pass

def solve(cnt, blue ,red):
    si = red[0]
    sj = red[1]



    # 레드 기준으로 방향 잡기
    for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        ni, nj = si + di, sj + dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '.':
            pass

    pass

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
print(arr)

blue_point = 0
red_point = 0
goal = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'B':
            blue_point = [i, j]
        if arr[i][j] == 'R':
            red_point = [i, j]
        if arr[i][j] == 'O':
            goal = [i, j]
    if blue_point != 0 and red_point != 0 and goal != 0:
        break
print(blue_point)
print(red_point)
print(goal)

# solve(0, blue_point, red_point)