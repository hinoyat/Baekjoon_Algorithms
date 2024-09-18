def robo(si, sj, di):
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1
    i = si
    j = sj
    d = di





    pass


N, M = int(input())
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