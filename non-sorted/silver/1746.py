import sys
input = sys.stdin.readline
n, m = map(int, input().split())
no_l = set()
no_s = set()

for i in range(n):
    no_l.add(input())

for j in range(m):
    no_s.add(input())

result = list(no_l & no_s)
result.sort()
print(len(result))
for i in result:
    print(i, end='')