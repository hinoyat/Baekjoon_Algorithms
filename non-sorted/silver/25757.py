need_player = {'Y':1, 'F':2, 'O':3}
N, game = input().split()

people_lst = set()
game_cnt = 0
people = 0
for i in range(int(N)):
    p = input()
    if p not in people_lst:
        people_lst.add(p)
#         people += 1
#     if people == need_player[game]:
#         game_cnt += 1
#         people = 0
# print(game_cnt)
print(len(people_lst)//need_player[game])