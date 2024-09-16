import heapq, sys

input = sys.stdin.readline
# 알고 스팟
def dijkstra(si,sj):
    que = []
    visited = [[9999] * M for _ in range(N)]
    heapq.heappush(que, (arr[si][sj], si, sj))
    while que:
        val, qi, qj = heapq.heappop(que)
        if (qi, qj) == (N-1, M-1):
            return val
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if 0<=ni<N and 0<=nj<M:
                newval = val + arr[ni][nj]
                if newval < visited[ni][nj]:
                    heapq.heappush(que,(newval, ni, nj))
                    visited[ni][nj] = newval


M, N = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(N)]
# print(arr)
print(dijkstra(0, 0))