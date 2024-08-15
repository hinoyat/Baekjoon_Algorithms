# N = int(input())
# data = [list(input()) for _ in range(N)]
# cnt_lst = []
# d = 0
#
# for r in range(N):
#     for c in range(N):
#         if data[r][c] == '1':
#             data[r][c] = 1
#             q = []
#             q.append([r, c])
#             cnt = 1
#             d += 1
#
#             while q:
#                 r, c = q.pop()
#                 for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
#                     if 0 <= r+dr < N and 0 <= c+dc < N and data[r+dr][c+dc] == '1':
#                         q.append([r+dr, c+dc])
#                         data[r+dr][c+dc] = 1
#                         cnt += 1
#             cnt_lst.append(cnt)
#
# cnt_lst.sort()
#
# print(d)
# for n in cnt_lst:
#     print(n)


# test_case = 10
# for tc in range(1, test_case + 1):
#     N = int(input())
#     buil = list(map(int, input().split()))
#     sun = 0
#     for s in range(2, N - 2):
#         b_lst = sorted(buil[s - 2:s + 3])
#         print(b_lst)
#         if buil[s] > b_lst[3]:
#             sun += buil[s] - b_lst[3]
#     # print(f'#{tc} {sun}')



T = int(input())
for tc in range(1, T+1):

    front_card = []     # 앞쪽 카드 리스트
    back_card = []      # 뒤쪽 카드 리스트

    N = int(input())        # 카드 수
    cards = input().split()  # 카드 리스트

    if N % 2 == 0: # 카드 개수 짝수
        for idx in range(N):
            if idx < int(N/2):
                front_card.append(cards[idx])
            else:
                back_card.append(cards[idx])

    else:          # 카드 개수 홀수
        for idx in range(N):
            if idx <= int(N/2): 
                front_card.append(cards[idx])
            else:
                back_card.append(cards[idx])


    print(f"#{tc}", end=' ')
    for i in range(len(back_card)): # 앞쪽 카드 리스트, 뒤쪽 카드리스트 하나씩 출력
        print(front_card[i], end=' ')
        print(back_card[i], end=' ')
    if len(front_card) != len(back_card): # 홀수개라면 앞쪽 카드 리스트 남은 한장 마져 출력
        print(front_card[-1], end=' ')

    print()