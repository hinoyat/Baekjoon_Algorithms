# N과M(1)
from itertools import combinations
from itertools import permutations
N, M = map(int, input().split())

lst = [i for i in range(1, N+1)]

# c = list(combinations(lst, M))
# for i in c:
#     print(*i)
c = list(permutations(lst, M))
for i in c:
    print(*i)