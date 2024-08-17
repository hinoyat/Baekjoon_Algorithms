# # 토마토
# def BFS(box):
#     visited = [[0]*boxj for _ in range(boxi)]
#     que = []
#     time = 0
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     for i in range(boxi):
#         for j in range(boxj):
#             if tomato_box[i][j] == 1 and visited[i][j] == 0:
#                 que.append([i, j])
#                 while que:
#                     ti, tj = que.pop()
#                     visited[ti][tj] = 1
#                     for d in range(4):
#                         ni = ti + di[d]
#                         nj = tj + dj[d]
#                         if 0<= ni < boxi and 0<= nj<boxj and visited[ni][nj] == 0 and tomato_box[ni][nj] ==0:
#                             tomato_box[ni][nj] = 1
#                             visited[ni][nj] = visited[ti][tj] + 1
#                             time += 1
#     return visited, time, box


# boxj, boxi, h = map(int, input().split())
# tomato_box = [list(map(int, input().split())) for _ in range(boxi)]

# deque가 훨씬 빨라서 임포트
from collections import deque
def BFS(box):
    # 익은 토마토를 바꿔주기 위해 글로벌 선언!
    global tomato_box
    # 방문기록장
    visited = [[[0]*boxj for _ in range(boxi)]for _ in range(boxh)]
    # deque는 그냥 우리가 배운 que처럼 사용
    que = deque()
    # 박스의 높이
    for h in range(boxh):
        # 박스의 행
        for i in range(boxi):
            # 박스의 열
            for j in range(boxj):
                # 처음에 1인 것(익은 토마토)을 다 que에 넣어줘요. 동시에 익는 것이 퍼지기 때문에
                if tomato_box[h][i][j] == 1 and visited[h][i][j] == 0:
                    que.append([h, i, j])
                    # 방문 체크해서 이상한 짓 안하게
                    visited[h][i][j] = 1

    while que:
        # 높이 행 열 팝 popleft는 가장 앞에 있는 원소를 가져와요
        th, ti, tj = que.popleft()
        
        # 토마토가 퍼지는 것은 윗 박스, 아래 박스, 동서남북
        for dh, di, dj in [[0, 1, 0], [0, -1, 0],[0, 0, 1], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]:
            nh = th + dh
            ni = ti + di
            nj = tj + dj
            if 0<= nh < boxh and 0<=ni<boxi and 0<= nj < boxj and tomato_box[nh][ni][nj] == 0 and visited[nh][ni][nj] == 0:
                que.append([nh, ni, nj])
                visited[nh][ni][nj] = visited[th][ti][tj] + 1
                tomato_box[nh][ni][nj] = 1
    # 방문할 때마다 1씩 늘려 줬으니 그것의 최댓값 저장할 변수
    max_t = 0
    # 만약 돌다가 안 익은 토마토가 있으면 -1 리턴
    for h in range(boxh):
        for i in range(boxi):
            for j in range(boxj):
                if tomato_box[h][i][j] == 0:
                    return -1
                if visited[h][i][j]> max_t:
                    max_t = visited[h][i][j]
        # -1 해주는 이유는 초기에 익어있는 토마토의 위치를 1로 표시했기 때문
    return max_t-1



boxj, boxi, boxh = map(int, input().split())
tomato_box = [[list(map(int, input().split())) for _ in range(boxi)]for _ in range(boxh)]
print(BFS(tomato_box))