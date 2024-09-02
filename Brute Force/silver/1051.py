N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

max_v = 1

for i in range(N):
    for j in range(M):
        for s in range(1, max(N, M)):
            ni = i + s
            nj = j + s
            nj2 = j - s
            if 0<= ni < N and 0 <= nj < M and 0<= nj2 < M:
                if arr[i][j] ==arr[ni][j] == arr[i][nj] == arr[ni][nj]:
                    v = (s+1)**2
                    if v > max_v:
                        max_v = v
            if 0<= ni < N and 0<= nj2 < M:
                if arr[i][j] ==arr[ni][j] == arr[i][nj2] == arr[ni][nj2]:
                    v = (s+1)**2
                    if v > max_v:
                        max_v = v

            else:
                break

print(max_v)