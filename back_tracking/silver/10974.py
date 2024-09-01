def back(result, cnt):
    if len(result) == N:
        ans.append(result[:])
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            result.append(lst[i])
            back(result, cnt + 1)
            visited[i] = 0
            result.pop()

N = int(input())
lst = [i for i in range(1, N+1)]

ans = []

visited = [0] * N

back([], 0)

# print(ans)
for i in ans:
    print(*i)