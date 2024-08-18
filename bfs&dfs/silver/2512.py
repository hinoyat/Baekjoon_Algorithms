n = int(input())
lst = list(map(int, input().split()))
total = int(input())
if sum(lst) > total:
    start = 1
    end = max(lst)
    # 돌면서 탐색
    max_v = 0
    while start <= end:
        mid = (start+end)//2
        sum_v = 0
        for i in lst:
            if i > mid:
                sum_v += mid
            else:
                sum_v += i
        if sum_v <= total:
            start = mid +1
            max_v = mid
        else:
            end = mid - 1
    # 
    print(max_v)
else:
    print(max(lst))