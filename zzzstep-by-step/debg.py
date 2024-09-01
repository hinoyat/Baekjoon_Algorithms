T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(input()) + [0] for _ in range(N)]
    password = ''
    password_set = set()
    for i in range(N):
        for j in range(M):
            if data[i][j] != '0':
                password += data[i][j]
            else:
                password_set.add(password)
                password = ''
    print(password)
    password_lst = []
    password_dict = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16}
    for lst in password_set:
        password = ''
        for n in lst:
            if n.isdecimal():
                n = int(n)
                password += bin(n)[2:]
            else:
                password += bin(password_dict[n])[2:]
        password_lst.append(password)

    print(password_lst, password_set)