# swea 이진 힙

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     Tree = [0] * (N+1)
#     # 부모노드 n 왼쪽 n*2 오른쪽 n*2+1

#     mother = 1
#     for i in lst:
#         Tree[mother] = i
        
#         check = mother
#         while check > 0 and Tree[check] < Tree[check//2]:
#             Tree[check], Tree[check//2] = Tree[check//2], Tree[check]
#             check//=2
#         mother += 1

#     r = N
#     result = 0
#     while r:
#         r//=2
#         result += Tree[r]
#     print(f'#{tc} {result}')

# T = int(input())
# for tc in range(1, T+1):
#     N, M, L = map(int,input().split())
#     tree = [0] * (N+1)
#     for i in range(M):
#         node, value = map(int, input().split())
#         tree[node] = value

#     start = L
#     result = 0
#     stack = []
#     stack.append(start)
#     while stack:
#         n = stack.pop()
#         result += tree[n]
#         left = n * 2
#         if left <= N:
#             stack.append(left)
#         right = n * 2 +1
#         if right <= N:
#             stack.append(right)
#     print(f'#{tc} {result}')

# 트리의 부모님 찾기
import sys
input = sys.stdin.readline
from collections import deque
def find_parent(start):
    result = [0] * (N+1)
    visited = [0] * (N+1)
    que = deque()
    que.append(start)
    while que:
        q = que.popleft()
        for d in tree[q]:
            if visited[d] == 0:
                que.append(d)
                visited[d] = 1
                result[d] = q
    return result[2:]


N = int(input())
tree = [[]for _ in range(N+1)]
for i in range(N-1):
    v1, v2 = map(int, input().split())
    tree[v1].append(v2)
    tree[v2].append(v1)

realresult = find_parent(1)
for i in realresult:
    print(i)