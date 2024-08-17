# 바이러스

def dfs(lst, start, N):
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    stack = []
    stack.append(start)
    virus = 0
    while stack:
        c = stack.pop()
        for i in lst[c]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                virus += 1
    return virus





N = int(input())
net = int(input())
lst = [[] for _ in range(N+1)]
for i in range(net):
    c1, c2 = map(int, input().split())
    lst[c1].append(c2)
    lst[c2].append(c1)
# print(lst)
start = 1
print(dfs(lst, start, N))