def supernova(cnt, idx, val):
    if cnt + val < 6:
        return

    if cnt == 6:
        print(*lst)
        return

    lst.append(N[idx])
    supernova(cnt + 1, idx + 1, val - 1)
    lst.pop()
    supernova(cnt, idx + 1, val - 1)

N = list(map(int,input().split()))
while N != [0]:
    num = N.pop(0)
    lst = []
    supernova(0, 0, num)
    print()

    N = list(map(int,input().split()))
