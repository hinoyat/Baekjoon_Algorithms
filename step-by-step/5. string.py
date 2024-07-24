# #27866
# string = input()
# st_num = int(input())
# print(string[st_num-1])

# # 2743
# string = input()
# print(len(string))

# # 9086
# st_num = int(input())
# for i in range(st_num):
#     string = input()
#     print(string[0],end='')
#     print(string[len(string)-1])


# # 11654
# s = input()
# print(ord(s))

# # 11720

# n = int(input())
# num_list = input()
# sum_num = 0
# for i in range(n):
#     s = num_list[i]
#     sum_num += int(s)

# print(sum_num)




# # 10809 이거 ord 써서 다시
# # s = input()
# # alpha = 'abcdefghijklmnopqrstuvwxyz'
# # check_list = []
# # for i in range(len(alpha)):
# #     if alpha[i] in s:
# #         for d in range(len(s)):  ### 이 코드의 오류는 첫번째 등장한 값만 저장해야 하는데
# #             if alpha[i] != s[d]:  ## 두 번 이상 등장할 경우, 두 번 리스트에 추가하게 된다
# #                 pass
# #             elif alpha[i] == s[d]:
# #                 check_list.append(d)
# #     if alpha[i] not in s:
# #         check_list.append(-1)
        
# # print(*check_list) 

# s = input()
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# check_list = []
# for i in range(len(alpha)):
#     if alpha[i] in s:
#         check_list.append(s.index(alpha[i]))    
#     if alpha[i] not in s:
#         check_list.append(-1)
        
# print(*check_list) 