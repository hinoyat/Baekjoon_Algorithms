def supernova(level, info):
    global ans
    val = int(''.join(info))
    if (val, level) in check:
        return

    check.add((val, level))
    if level == N:
        ans = max(ans ,val)
        return


    for i in range(len(info)):
        for j in range(len(info)):
            if i != j:
                if info[j] == '0':continue
                info[i], info[j] = info[j], info[i]
                supernova(level + 1, info)
                info[i], info[j] = info[j], info[i]




info = list(input())
N = int(info.pop())
info.pop()
ans = -1
check = set()
# print(info, N)
supernova(0, info)
print(ans)