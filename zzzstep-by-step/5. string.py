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

# # 2675
# t = int(input())

# for _ in range(t):
#     r, s = list(map(str, input().split()))
#     for i in s:
#         print(i*int(r), end='')
#     print()



# # 1152 단어의 개수 - 파이썬에서만 쉽대
# string = list(input().split())

# print(len(string))



# # 2908 상수

# a, b = map(str,input().split())

# rev_a = a[::-1]
# rev_b = b[::-1]

# if int(rev_a) > int(rev_b):
#     print(rev_a)
# else:
#     print(rev_b)


# # 5622 다이얼  time 기본 세팅값에 따라 뒤의 코드가 달라짐
# string = input()

# # print(ord('A')) # 65
# # print(ord('Z')) # 90
# time = 0
# for i in string:
#     if 65 <= ord(i) <68:
#         time += 3
#     elif 68 <= ord(i) <71:
#         time += 4
#     elif 71 <= ord(i) <74:
#         time += 5
#     elif 74 <= ord(i) <77:
#         time += 6
#     elif 77 <= ord(i) <80:
#         time += 7
#     elif 80 <= ord(i) <84:
#         time += 8
#     elif 84 <= ord(i) <87:
#         time += 9
#     elif 87 <= ord(i) <91:
#         time += 10

# print(time)


# # 11718 그대로 출력하기 Vscode EOF = ctrl z 파이참 d
# while True:
#     try:
#         x = print(input())

#     except:
#         break