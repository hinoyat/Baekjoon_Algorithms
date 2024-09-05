# import sys
# input = sys.stdin.readline
#
# def supernova(si, sj, sum_v):
#     global min_v
#
#     if sum_v > min_v:
#         return
#
#     if (si, sj) in memo and sum_v >= memo[(si, sj)]:
#         return
#
#     memo[(si, sj)] = sum_v
#
#     if si == N-1 and sj == N-1:
#         if sum_v < min_v:
#             min_v = sum_v
#
#     for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
#         ni = si + di
#         nj = sj + dj
#         if ni < 0 or nj < 0 or ni >= N or nj >= N or visited[ni][nj]!= 0:
#             continue
#         else:
#             visited[ni][nj] = 1
#             supernova(ni, nj, sum_v + arr[ni][nj])
#             visited[ni][nj] = 0
#
#
# N = int(input())
# cnt = 1
# while N != 0:
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     visited = [[0]*N for _ in range(N)]
#     min_v = 21e8
#     memo = {}
#     supernova(0, 0, arr[0][0])
#
#     print(f'Problem {cnt}: {min_v}')
#     N = int(input())
#     cnt += 1


import heapq
import sys

input = sys.stdin.readline


def dijkstra():
    # Priority queue for Dijkstra's algorithm (min-heap)
    pq = [(arr[0][0], 0, 0)]  # (current_sum, i, j)
    min_sum = [[float('inf')] * N for _ in range(N)]
    min_sum[0][0] = arr[0][0]

    while pq:
        current_sum, si, sj = heapq.heappop(pq)

        if si == N - 1 and sj == N - 1:
            return current_sum

        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = si + di, sj + dj

            if 0 <= ni < N and 0 <= nj < N:
                new_sum = current_sum + arr[ni][nj]

                if new_sum < min_sum[ni][nj]:
                    min_sum[ni][nj] = new_sum
                    heapq.heappush(pq, (new_sum, ni, nj))

    return float('inf')


# Main code execution
cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra()
    print(f'Problem {cnt}: {result}')
    cnt += 1
