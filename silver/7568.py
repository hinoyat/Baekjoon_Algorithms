N = int(input())

information = []
for p in range(N):
    pe = list(map(int, input().split()))
    information.append(pe)

rank_lst = []

for i in range(N):
    rank = 1
    for j in range(N):
        if i != j :
            if information[i][0] < information[j][0] and information[i][1] < information[j][1]:
                rank += 1
    rank_lst.append(rank)

print(*rank_lst)