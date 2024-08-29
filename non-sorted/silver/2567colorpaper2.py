from pprint import pprint
N = 100
arr = [[0 for _ in range(N+2)]for _ in range(N+2)]
paper = int(input())
p_l = 10

for s in range(paper):
    pi, pj = map(int, input().split())
    for i in range(pi+1, pi+p_l+1):
        for j in range(pj+1, pj+p_l+1):
            if i <= N and j <= N:
                arr[i][j] = 1

# print(max_i, max_j)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
cnt = 0
for i in range(N+2):
    for j in range(N+2):
        if arr[i][j] == 0:
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if 0<= ni < N+2 and 0<= nj < N+2:
                    if arr[ni][nj] == 1:
                        cnt += 1

print(cnt)