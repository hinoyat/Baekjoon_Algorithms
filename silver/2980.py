N, L = map(int, input().split())
road = [0 for _ in range(L+1)]
light = [[] for _ in range(L+1)]
for i in range(N):
    p, red, green = map(int, input().split())
    road[p] = 1
    light[p] = [red, green]
# print(road)
# print(light)

start_p = 0
cur_p = 0
time = 0

while cur_p <= L:
    if road[cur_p] == 0:
        cur_p += 1
        time += 1
    else:
        red = light[cur_p][0]
        green = light[cur_p][1]
        cycle = red + green
        if red == green:
            if (time//red)%2 !=0 and 0< time%red <=green:
                time += 1
                cur_p += 1
            else:
                time += 1
        else:
            if 0 < time % red <= green:
                time += 1
                cur_p += 1
            else:
                time += 1
    

print(time)
