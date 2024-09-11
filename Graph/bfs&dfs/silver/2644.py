people = int(input())
# 촌수 계산
def Bfs(find1, find2):
    visited = [0 for _ in range(people+1)]
    visited[find1] = 1
    que = []
    que.append(find1)
    while que:
        r = que.pop(0)
        for i in lst[r]:
            if visited[i] == 0:
                visited[i] = visited[r] + 1
                que.append(i)
    if visited[find1] >0 and visited[find2] > 0:

        result = abs(visited[find2] - visited[find1])
    else:
        result = -1
    
    return result



find1, find2 = map(int, input().split())
rel = int(input())
lst = [[] for _ in range(people+1)]
for i in range(rel):
    p1, p2 = map(int, input().split())
    lst[p1].append(p2)
    lst[p2].append(p1)

print(Bfs(find1, find2))