from collections import deque

def baaaaaaaaaaaaaam(si, sj):
    que = deque()
    que.append((si, sj))
    di = 0
    ni = si
    nj = sj
    time = 0
    while que:
        ni, nj = ni + direction[di][0], nj + direction[di][1]
        # print(que)
        # print(ni,nj, di)
        time += 1
        # 벽에 부딪히다
        if ni < 0 or nj < 0 or ni >= N or nj >= N:
            break

        # 자기 꼬리에 부딪히다

        if (ni, nj) in que:
            break

        # 이동하기 # 사과가 아니면
        if arr[ni][nj] == 0:
            # 머리 넣고
            que.append((ni, nj))
            # 꼬리 빼고
            que.popleft()

        # 이동하기 # 사과면
        elif arr[ni][nj] == 100:
            #머리 넣기
            que.append((ni,nj))
            # 사과 먹기
            arr[ni][nj] = 0

        # 시간 추가

        # 바꿀 시간 되면
        if time in order:
            order_order = order[time]
            if order_order == 'L':
                di = direction[di][2]
            elif order_order == 'D':
                di = direction[di][3]
                
        # if time == end_time:
        #     break

    return time

            #우 -> 상   상 -> 좌   좌 -> 하    하 _> 우
            #우 -> 하   상 -> 우   좌 -> 상    하 _> 좌
direction = {0:(0, 1, 1, 3), 1:(-1, 0, 2, 0), 2:(0, -1, 3, 1), 3:(1, 0, 0, 2)}


N = int(input())
arr = [[0] * N for _ in range(N)]
# 먼저 들어오면 머가리
# 늦게 들어오면 꼬리

apple_num = int(input())
for _ in range(apple_num):
    ai, aj = map(int,input().split())
    arr[ai-1][aj-1] = 100

order_num = int(input())
order = {}
end_time = 0
for _ in range(order_num):
    c, d = input().split()
    # order.append(d)
    order[(int(c))] = d
    end_time = max(end_time, int(c))
# print(order)
# print(arr)
start_point = [0, 0, 0]
print(baaaaaaaaaaaaaam(0, 0))
