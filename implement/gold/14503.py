def robo(si, sj, di):
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1
    ans = 1
    ni = si
    nj = sj
    nd = di
    while True:
        # di, dj = direction[nd][0], direction[nd][1]

        # 현재 칸에서 주변을 돌아보기
        can = False
        cnt = 0
        while cnt <= 3:
            nd = direction[nd][2]
            if nd >= 4:
                nd = 0
            ci, cj = ni + direction[nd][0], nj + direction[nd][1]
            if 0 <= ci < N and 0 <= cj < M:
                if arr[ci][cj] == 0 and visited[ci][cj] == 0:
                    can = True
                    ni, nj = ci, cj
                    break
                else:
                    cnt += 1
            else:
                cnt += 1

        if can == False:
            ni, nj = ni - direction[nd][0], nj - direction[nd][1]
            if arr[ni][nj] == 1:
                return ans
        else:
            visited[ni][nj] = 1
            ans += 1


N, M = map(int, input().split())
robox, roboy, firstd = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = {0:(1, 0, 3), 1:(0, 1, 0), 2:(-1, 0, 1), 3:(0, -1, 2)}


# 주변에 빈 칸이 없으면
# 뒤가 벽이 아니면 후진
# 벽이면 작동 중지

# 0 북, 1 동, 2 남, 3 서
# 빈칸이 있으면
# 1. 90도 회전
# 2. 한칸 전진


# 현재 칸이 청소 X 청소 -> 방문처리 청소는 -1로 하자

direction = {0 : (-1, 0, 3), 1 : (0, 1, 0), 2 : (1, 0, 1), 3 : (0, -1, 2)}

print(robo(robox, roboy, firstd))
