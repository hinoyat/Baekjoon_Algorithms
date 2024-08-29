# 보물
N = int(input())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

a_lst.sort()

visit_b = [0*N for _ in range(N)]
pop_cnt = 0

val = 0
while pop_cnt <N:
    max_b = -1
    visit = []
    for i in range(len(b_lst)):
        if visit_b[i] == 0:
            if b_lst[i] >= max_b:
                max_b = b_lst[i]
                visit.append(i)
    s = visit.pop()
    visit_b[s] = 1
    pop_cnt += 1
    min_a = a_lst.pop(0)
    val += max_b * min_a
print(val)