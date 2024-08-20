# 수 정렬하기
import sys
input = sys.stdin.readline
N = int(input())
dct = {}

for i in range(N):
    n = int(input())
    if n in dct:
        dct[n]+= 1
    else:
        dct[n] = 1
 
key = list(dct.keys())
key.sort()

for i in key:
    for j in range(dct[i]):
        print(i)