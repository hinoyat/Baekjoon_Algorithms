# # 25083 새싹

# print("""         ,r'"7
# r`-_   ,'  ,/
#  \\. ". L_r'
#    `~\\/
#       |
#       |""")


# # # 3003 킹, 퀸, 룩, 비숍, 나이트, 폰
# chess = [1, 1, 2, 2, 2, 8]
# num = list(map(int,input().split()))
# result = []

# for i in range(6):
#     need = chess[i] - num[i]
#     result.append(need)

# print(*result)


# # 2444  다시 다시 다싣 ㅏ싣다ㅣ
# n = int(input())
# center = 2*n-1
# star = '*'
# blk = ' '
# for i in range(1,n+1):

#     print((blk*(n-(i))),end='')
#     print(star * ((i*2)-1))

# for i in range(n-1,0,-1):

#     print(blk * (n-(i)),end='')
#     print(star*((i*2)-1))


# # 10988 펠린드롬  인덱스 슬라이싱

# string = input()
# str_len = len(string)

# check_lst =[]
# if str_len % 2 == 0:
#     if len(string) % 2 == 0:
#         for i in range(0, str_len//2):
#             if string[i] == string[str_len-i-1]:
#                 check_lst.append(1)
#             else:
#                 check_lst.append(0)
# else:
#     for i in range(0, str_len//2):
#         if string[i] == string[str_len-i-1]:
#             check_lst.append(1)
#         else:
#             check_lst.append(0)



# if 0 in check_lst:
#     print(0)
# else:
#     print(1)