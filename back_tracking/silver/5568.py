def back(result, cnt):
    global visited
    global ans

    if cnt == K:
        if result not in check:
            check.add(result)
            ans += 1
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            # 카드 추가
            new_result = result + card[i]
            back(new_result, cnt + 1)
            # 카드 제거
            visited[i] = 0

N = int(input())
K = int(input())
card = [input().strip() for _ in range(N)]
ans = 0
check = set()
visited = [0] * N
back('', 0)
print(ans)
