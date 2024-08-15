from pprint import pprint
H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]
# print(arr)
i = 0
j = 0
cl = -1
while i<H:
    if arr[i][j] == 'c':
        cl = 0
        arr[i][j] = 0
    else:
        if cl != -1:
            cl+= 1
            arr[i][j] = cl
        else:
            cl = -1
            arr[i][j] = cl
    j += 1
    if j >=W:
        i += 1
        j = 0
        cl = -1

for i in arr:
    print(*i)