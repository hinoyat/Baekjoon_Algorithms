# 카드 2
from collections import deque
N = int(input())
dq = deque()
for i in range(1, N+1):
    dq.append(i)

while len(dq) >  1:
    dq.popleft()
    a = dq.popleft()
    dq.append(a)
print(*dq)