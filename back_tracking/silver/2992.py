def back(result, cnt):
    global ans
    global visited
    if cnt == stop_point:
        if int(result) > N:
            if int(result) < ans:
                ans = int(result)


    for i in range(stop_point):
        if visited[i] == 0:
            visited[i] = 1
            new_result = result + check[i]
            back(new_result, cnt + 1)
            visited[i] = 0




N = int(input())
ans = 10000000
check = list(str(N))
# print(check)
stop_point = len(check)
visited = [0]*stop_point

back('', 0)
if ans == 10000000:
    ans = 0
print(ans)