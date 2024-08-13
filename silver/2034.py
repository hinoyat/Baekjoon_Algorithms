# + 기준 A = 0, B = 2, C = 3, D = 5, E = 7, F = 8, G = 10
# -1 일 때 7 -2 일 떄 5 - 8일 때 7
# + 10일 때 G +11일 때 A
n = int(input())
# p리스트 for문
p_lst = []
for _ in range(n):
    p = int(input())
    p_lst.append(p)
lst = ['A', 0, 'B', 'C', 0, 'D', 0, 'E', 'F', 0, 'G', 0]
print(len(lst))
print(p_lst)

for i in range(lst):
    if lst[i]!= 0:
        idx = 0
        while True:
            if i - p_lst[idx] < 0