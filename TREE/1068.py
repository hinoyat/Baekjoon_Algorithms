def supernova(d):
    tree[d] = -999
    for i in range(N):
        if tree[i] == d:
            supernova(i)

N = int(input())
tree = list(map(int, input().split()))
del_num = int(input())
supernova(del_num)

ans = 0
check = set(tree)
# print(tree)
for i in range(N):
    if tree[i] != -999 and i not in check:
        ans += 1
print(ans)
