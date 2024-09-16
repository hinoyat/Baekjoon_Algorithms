N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

RGB = 3

for i in range(1, N):
    for j in range(RGB):
        arr[i][j] = min(arr[i - 1][(j+1)%3], arr[i - 1][(j + 2)%3]) + arr[i][j]

print(min(arr[N - 1]))