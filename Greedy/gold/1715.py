import heapq, sys
input = sys.stdin.readline
N = int(input())
que = []
for _ in range(N):
    heapq.heappush(que, int(input()))

ans = 0
while True:
    if len(que) == 1:
        break
    q1 = heapq.heappop(que)
    q2 = heapq.heappop(que)
    q3 = q1 + q2
    ans += q3
    heapq.heappush(que, q3)
print(ans)

