# 프린터 큐
from collections import deque
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    q[M] = -1
    p = False
    while p == True:
        