def back(result, cnt):
    if len(result) == N:
        ans.append(result[:])
        return

    for i in range(M):
        if visited[i] == 0:
            visited[i] = 1
            result.append(lst[i])
            back(result, cnt + 1)
            visited[i] = 0
            result.pop()

M, N = map(int,input().split())
lst = [i for i in range(1, M+1)]

ans = []

visited = [0] * M

back([], 0)

# print(ans)
for i in ans:
    print(*i)