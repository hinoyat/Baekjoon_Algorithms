from pprint import pprint as p
# 단지 번호 붙이기
def Dfs():
    stack = []
    visited = [[0]* N for _ in range(N)]
    h = 1
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    apart = 0
    home = []
    for i in range(N):
        for j in range(N):
            cnt = 0
            if arr[i][j] == '1' and visited[i][j] == 0:
                stack.append([i, j])
                visited[i][j] = h
                cnt += 1
                while stack:
                    pi, pj = stack.pop()
                    for d in range(4):
                        ni = pi + di[d]
                        nj = pj + dj[d]
                        if 0<= ni<N and 0<=nj<N and visited[ni][nj]==0 and arr[ni][nj]=='1':
                            stack.append([ni,nj])
                            visited[ni][nj] = h
                            cnt +=1
                home.append(cnt)
                apart += 1
                h += 1
    home.sort()
    return [apart, *home]


N = int(input())
arr = [list(input()) for _ in range(N)]
# p(arr)
result = Dfs()
for r in result:
    print(r)