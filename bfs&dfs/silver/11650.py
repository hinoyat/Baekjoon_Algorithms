# 좌표정렬
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    a = list(map(int, input().split()))
    lst.append(a)

lst.sort()


for a, b in lst:
    print(a, b)