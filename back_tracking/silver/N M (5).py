def supernova(idx, cnt, val):
    # if idx > N:
    #     return

    if cnt == M:
        print(*check)
        return

    # if val + cnt < M:
    #     return

    for i in range(N):
        if not visited[i]:
            check.append(num_lst[i])
            visited[i] = 1
            supernova(idx + 1, cnt + 1, val - 1)
            check.pop()
            visited[i] = 0
    # supernova(idx + 1, cnt, val - 1)


N, M = map(int, input().split())
num_lst = list(map(int,input().split()))
num_lst.sort()
check = []
visited = [0] * N
supernova(0, 0, N)