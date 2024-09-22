T = int(input())
for tc in range(T):
    round = int(input())
    info = list(map(int, input().split()))
    team_cnt = max(info)
    team_point = [0] * (team_cnt + 1)

    team_player = [0] * (team_cnt + 1)

    fifth_player_point = [0] * (team_cnt + 1)

    winner = 0

    min_point = 99999

    temp = [0] * (team_cnt + 1)

    check = set()

    for i in range(round):
        temp[info[i]] += 1
        if temp[info[i]] == 6:
            check.add(info[i])

    point = 1

    for i in range(round):
        if info[i] not in check: continue
        team_player[info[i]] += 1
        # team_point[info[i]] += point
        if team_player[info[i]] <= 4:
            team_point[info[i]] += point
        point += 1

        if team_player[info[i]] == 5:
            fifth_player_point[info[i]] = point - 1
        elif team_player[info[i]] == 6:
            # 먼저 들어온 곳과 5번째 선수 비교
            if team_point[info[i]] < min_point:
                min_point = team_point[info[i]]
                winner = info[i]
            elif team_point[info[i]] == min_point:
                if fifth_player_point[info[i]] < fifth_player_point[winner]:
                    winner = info[i]

    print(winner)

