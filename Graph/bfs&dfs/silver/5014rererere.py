# 스타트링크
from collections import deque


def supernova(cur, end):
    que = deque()
    que.append(cur)
    visited[cur] = 1
    while que:
        q = que.popleft()
        if q == end:
            return visited[q] - 1
        for new in (q + U, q - D):
            if new <= F and visited[new] == 0 and new > 0:
                visited[new] = visited[q] + 1
                que.append(new)

    return 'use the stairs'

# 층, 시작, 목표, 위로 U칸, 아래로 D칸
F, S, G, U, D = map(int, input().split())
ans = 1000001
visited = [0] * (F+1)
print(supernova(S, G,))
