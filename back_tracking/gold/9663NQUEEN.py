def check(row, col):
    for i in range(row):
        if arr[i][col] == 1:
            return False


    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if arr[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if arr[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def nqueen(idx):
    global ans
    if idx == N:
        ans += 1
        return

    for j in range(N):
        if check(idx, j):
            arr[idx][j] = 1
            nqueen(idx + 1)
            arr[idx][j] = 0

N = int(input())

arr = [[0] * N for _ in range(N)]

visited_col = [0] * N

ans = 0

nqueen(0)

print(ans)

