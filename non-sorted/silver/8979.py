N, K = map(int, input().split())
diction = {}
gold = 1000000000001
silver = 1000001
bronze = 1
find_c_v = 0
for i in range(N):
    c, g, s, b = map(int, input().split())
    value = g*gold + s*silver + b*bronze
    if not value in diction:
        diction[value] = [c]
    else:
        diction[value].append(c)
    if c == K:
        find_c_v = g*gold + s*silver + b*bronze
# print(diction)

key = list(diction.keys())
key.sort(reverse=True)
rank = 1

for i in key:
    if K in diction[i]:
        break
    else:
        if len(diction[i]) == 1:
            rank +=1
        else:
            rank += len(diction[i])
print(rank)
