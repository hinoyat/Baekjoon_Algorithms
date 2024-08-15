T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    n = lst.pop(0)
    # print(lst)
    sorted_lst = []
    pop_cnt = 0
    cnt = 0
    while pop_cnt < 20:
        s = lst.pop(0)
        if not sorted_lst:
            sorted_lst.append(s)
        else:
            for i in sorted_lst:
                if i > s:
                    cnt += 1
            sorted_lst.append(s)
            sorted_lst.sort()
        pop_cnt += 1
    print(n, cnt)

