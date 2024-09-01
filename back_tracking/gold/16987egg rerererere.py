import sys
input = sys.stdin.readline


def backtrack(info, idx, cnt):
    global boom


    if idx == N:
        if cnt > boom:
            boom = cnt
        return

    if info[idx][0] <= 0:
        backtrack(info, idx+1, cnt)
    else:
        flag = False
        for i in range(N):
            if idx == i or info[i][0] <= 0:
                continue
            flag = True
            count = 0
            info[idx][0] -= info[i][1]
            info[i][0] -= info[idx][1]

            if info[idx][0] <= 0:
                count += 1
            if info[i][0]<= 0:
                count += 1

            backtrack(info, idx+1, cnt + count)

            info[idx][0] += info[i][1]
            info[i][0] += info[idx][1]
        if flag == False:
            backtrack(info, idx+1, cnt)

N = int(input())
lst = []
for i in range(N):
    info = list(map(int, input().split()))
    lst.append(info)

boom = 0

backtrack(lst, 0, 0)
print(boom)
