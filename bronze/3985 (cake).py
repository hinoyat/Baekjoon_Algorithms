L = int(input())
N = int(input())
lst = [[] for _ in range(N+1)]
ex_get_cake = [0 for _ in range(N+1)]
get_cake = [0 for _ in range(N+1)]
cake = [1 for _ in range(L)]
# print(lst)
# print(cake)

for i in range(1, N+1):
    P, K = map(int, input().split())
    lst[i] = [P, K]
# print(lst)

ex = 0
real = 0

for i in range(1, len(lst)):
    p, k = lst[i]
    ex_get_cake[i] = k - p
    # 진짜 받은 사람
    for j in range(p-1, k):
        if cake[j] == 1:
            get_cake[i] += 1
            cake[j] -= 1
            # print(cake)

for i in range(len(ex_get_cake)):
    if ex_get_cake[i] == max(ex_get_cake):
        expected = i
        break

for i in range(len(get_cake)):
    if get_cake[i] == max(get_cake):
        real = i
        break

print(expected)
print(real)
