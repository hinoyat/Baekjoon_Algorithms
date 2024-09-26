import pprint

def tornado(i, j):
    value = arr[i][j]
    # y/ a/ 5/ 1/ 1/ 7/ 7/ 10/ 10/ 2/ 2
    change1 = [[i, j-1], [i, j - 2], [i, j - 3],
               [i-1, j], [i + 1, j], [i - 1, j - 1], [i + 1, j - 1], [i - 1, j - 2], [i + 1, j - 2],
               [i - 2, j - 1], [i + 2, j - 1]]





# 마법사 상어와 토네이도
# N은 항상 홀수 5이면 2,2 시작 9이면 4,4 시작 start
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

start_point = [N//2, N//2]

# 45퍼센트가 주위 칸 나머지는 토네이도가 부는 칸


visited = [[0] * N for _ in range(N)]

pprint.pprint(visited)

direction = {0 : (0, -1), 1 : (1, 0), 2 : (0, 1), 3 : (-1, 0)}
end_point = (0, 0)

ni, nj = start_point[0], start_point[1]
visited[ni][nj] = 1
di = 0
cnt = 0
move_cnt = 0
max_move_cnt = 1
while (ni, nj) != (0, 0):
    tornado()



    ni, nj = ni + direction[di][0], nj + direction[di][1]
    visited[ni][nj] = 1
    cnt += 1
    if cnt == max_move_cnt:
        move_cnt += 1
        di = (di + 1) % 4
        cnt = 0
        if move_cnt == 2:
            max_move_cnt += 1
            move_cnt = 0
    # print(ni, nj)

pprint.pprint(visited)