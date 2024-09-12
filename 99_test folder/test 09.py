import sys

input = sys.stdin.readline
N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
lst.sort(key=lambda x:(x[1], x[0]))
# print(lst)


start_time = lst[0][1]
ans = 1
for i in range(1, N):
    if lst[i][0] >= start_time:
        start_time = lst[i][1]
        ans += 1

print(ans)