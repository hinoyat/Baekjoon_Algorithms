need = ['a', 'e', 'i', 'o', 'u']
while True:
    s = input()
    if s == 'end':
        break

    n_cnt = 0
    # 모음이 있는지 없는지 cnt 가 0이면 탈락
    for n in need:
        if n in s:
            n_cnt += 1

    # 모음 3개 연속
    mo = 0
    ja = 0
    for i in s:
        if i in need:
            mo += 1
            ja = 0

        if i not in need:
            mo = 0
            ja += 1

        if mo >=3 or ja >= 3:
            break
    can = 1
    if len(s)> 1:
        for j in range(len(s) - 1):
            if s[j] == s[j+1]:
                if s[j] == 'e' or s[j] == 'o':
                    pass
                else:
                    can = 0

    if n_cnt == 0 or mo >= 3 or ja >= 3 or can == 0 :
        print(f'<{s}> is not acceptable.')
    else:
        print(f'<{s}> is acceptable.')
