'''
## 2
4 11
..XXX...X..
.X.XXX...L.
....XXX..X.
X.L..XXX...

## 3
10 2
.L
..
XX
XX
XX
XX
XX
XX
..
.L

## 2
8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...
'''

def removeice(que):
    global ice
    new_que = que
    check = set()
    while que:
        qi, qj = que.popleft()
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if ni < 0 or nj < 0 or ni >= R or nj >= C or arr[ni][nj] == '.' or arr[ni][nj] == 'L': continue
            # ice.add((ni, nj))
            if arr[ni][nj] == 'X':
                if (ni, nj) in ice:
                    check.add((ni, nj))
                    new_que.append((ni, nj))
    print(check)
    return new_que

def move(bird):
    bi1, bj1 = bird[0][0], bird[0][1]
    bi2, bj2 = bird[1][0], bird[1][1]
    visited = [[0] * C for _ in range(R)]
    check_que = deque()
    flag = False
    check_que.append((bi1, bj1))
    while check_que:
        qi, qj = check_que.popleft()
        if (qi, qj) == (bi2, bj2):
            flag = True
            break
        for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ni, nj = qi + di, qj + dj
            if ni < 0 or nj < 0 or ni >= R or nj >= C or visited[ni][nj]: continue
            if arr[ni][nj] == 'X':
                if (ni, nj) in ice:
                    check_que.append((ni, nj))
                    visited[ni][nj] = 1
            else:
                check_que.append((ni, nj))
                visited[ni][nj] = 1

    if not flag:
        return False
    else:
        return True

def solve(time, que, bird):

    new_que = que
    while True:
        if move(bird):
            return time
        # 얼음 지워주기
        time += 1
        new_que = removeice(que)


    return time



# 백조의 호수
from pprint import pprint
from collections import deque
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
pprint(arr)
# 물 공간은 . or L
# 필요한 작업
# 시간 체크 함수 한 번 돌 때 마 따 시 간 1 씩 증 가
# 얼음의 좌표 담기 set BFS에서 만날 때 remove 해주기
ice = set()

bird = []

for i in range(R):
    for j in range(C):
        if arr[i][j] == '.' or arr[i][j] == 'L':
            for di, dj in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= R or nj >= C or arr[ni][nj] == '.' or arr[ni][nj] == 'L' or (ni, nj) in ice:continue
                ice.add((ni, nj))
        if arr[i][j] == 'L':
            bird.append((i, j))



first_que = deque(list(ice))
print(solve(0, first_que, bird))