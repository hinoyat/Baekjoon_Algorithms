# 1182 부분 수열의 합
def back(idx):
    global cnt
    if len(result) == i:
        if sum(result) == S:
            cnt += 1
        return
    else:
        for j in range(idx, N):
            if visited[j] == 0:
                visited[j] = 1
                result.append(lst[j])
                back(j + 1)
                result.pop()
                visited[j] = 0



N, S = map(int,input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(1,N+1):
    result = []
    visited = [0] * N
    back(0)
print(cnt)