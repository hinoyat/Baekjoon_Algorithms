N, M, R = map(int,input().split())
items = [0] + list(map(int, input().split()))
graph = [[]for _ in range(N + 1)]
for _ in range(R):
    val, a, b = map(int, input().split())