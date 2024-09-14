N, M = map(int, input().split())

# M개의 공유기를 설치 해

lst = list(int(input()) for _ in range(N))
lst.sort()
# print(lst)

start = 1
end = max(lst)+1
ans = 0
while start <= end:
    mid = (start + end)//2
    now = lst[0]
    cnt = 1

    for i in range(1, N):
        if lst[i] - now >= mid:
            cnt += 1
            now = lst[i]

    if cnt >= M:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
    # print(mid)
print(ans)