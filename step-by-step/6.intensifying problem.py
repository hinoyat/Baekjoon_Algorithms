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



# # 1157 단어 공부

# s = input()
# s_lower = s.lower() # 입력 문자 소문자로
# s_lst = list(s_lower) # 문자열 리스트로 변환
# check_lst = list(set(s_lower)) # 중복 제거한 리스트

# max_lst = []

# # print(s_lst)
# # print(check_lst)

# max = 0 #최다 등장 횟수

# # 최다 등장 횟수 구하기
# for i in check_lst:
#   num = s_lst.count(i)
#   if num > max:
#     max = num

# # print(max)

# # 최다 등장 알파벳 리스트
# # 문자열 리스트를 다시 순회하며 최다 등장 값이랑 같은 문자를 새로운 리스트에 추가
# for i in check_lst:
#   if s_lst.count(i) == max:
#     max_lst.append(i) 

# # 추가한 리스트에 1개 이상의 문자가 있다면 '?' 반환
# # 1개라면 대문자로 정상 출력
# if len(max_lst) == 1:
#   print(max_lst[0].upper())
# else:
#   print('?')




# # 2941 크로아티아 알파벳
# ### 1
# # 체크 할 크로아티아 문자 리스트
# check_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']
# cnt = 0       # 몇 개 들어있는지 확인

# s= input()

# for i in check_list:

#   if s.find(i) == -1:   # i가 없으면 .find()는 -1을 반환
#     pass                

#   else:                 
#     cnt_up = s.count(i)
#     cnt += cnt_up
#     for d in range(s.count(i)):
#       s = s.replace(i,'*')

# result = len(s)

# print(result)

# ### 2
# check_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# s= input()

# for i in check_list:

#   if s.find(i) == -1:   # i가 없으면 .find()는 -1을 반환
#     pass                
#   else:                 
#     s = s.replace(i,'*')

# result = len(s)

# print(result)


# ## 1316 그룹 단어 체커

# n = int(input())
# # 그룹 단어가 아닌 수
# not_group_cnt = 0

# for _ in range(n):
#     s = input()
#     # 단어를 순회하며 다른 문자가 나올 경우 나왔던 단어 추가
#     poped_lst = []
#     # 인덱스 에러 방지 전체 길이 - 1
#     for i in range(len(s)-1):
#       # pop list에 있는 문자가 또 나오면 카운트
#       if s[i] and s[i+1] in poped_lst:
#         not_group_cnt += 1
#         break
#       if s[i] == s[i+1]:
#         pass
#       # 문자가 달라질 경우 이전 문자 pop 리스트에 추가 
#       elif s[i] != s[i+1]:
#         poped_lst.append(s[i])
    
#     # print(poped_lst)
# # 결과는 전체 입력 개수 - 그룹 단어가 아닌 수
# result = n - not_group_cnt
# print(result)


# # 25206   왜 틀렸는지 생각을 해보세요
# # 입력을 받는다
# # 입력한 값을 딕셔너리로 만든다. 과목 : 학점 : 등급 :
# # 학점별로 곱하는 값을 할당

# std_dict = {}

# for i in range(20):
#     chihoon = list(map(str,input().split()))
#     std_dict[chihoon[0]] = [chihoon[2],chihoon[1]]

# grade_lst = list(std_dict.values())

# # 유효 성적 담을 리스트
# sum_lst = []

# # 수강 학점의 합
# gp_point_lst = []

# # 유효 성적 담기
# # 부동 소수점 포함 숫자를 계산하기 위해서는 int()가 아닌 float()
# for s in grade_lst:
#     if s[0] == 'A+':
#         gp_point = 4.5
#         sum_lst.append(gp_point * float(s[1]))
#         gp_point_lst.append(gp_point)
#     elif s[0] == 'A0':
#         gp_point = 4.0
#         sum_lst.append(gp_point* float(s[1]))
#         gp_point_lst.append(gp_point)
#     elif s[0] == 'B+':
#         gp_point = 3.5
#         sum_lst.append(gp_point* float(s[1]))
#         gp_point_lst.append(gp_point)
#     elif s[0] == 'B0':
#         gp_point = 3.0
#         sum_lst.append(gp_point* float(s[1]))
#         gp_point_lst.append(gp_point)
#     elif s[0] == 'C+':
#         gp_point = 2.5
#         sum_lst.append(gp_point* float(s[1]))
#         gp_point_lst.append(gp_point)
#     elif s[0] == 'C0':
#         gp_point = 2.0
#         sum_lst.append(gp_point* float(s[1]))
#         gp_point_lst.append(gp_point)
#     elif s[0] == 'D+':
#         gp_point = 1.5
#         sum_lst.append(gp_point* float(s[1]))
#         gp_point_lst.append(gp_point)
#     elif s[0] == 'D0':
#         gp_point = 1.0
#         sum_lst.append(gp_point* float(s[1]))
#         gp_point_lst.append(gp_point)
#     elif s[0] == 'F':
#         gp_point = 0
#         sum_lst.append(gp_point* float(s[1]))
#         gp_point_lst.append(gp_point)
#     else:
#         pass   

# # 학점 총합 구하기
# sum_gp = 0
# for i in sum_lst:
#     sum_gp += i

# # 수강 학점의 합
# sum_gp_point = 0
# for i in gp_point_lst:
#     sum_gp_point += i

# # 학점

# gp = sum_gp/sum_gp_point
# result = gp
# # print(std_dict)
# # print(type(grade_lst[0][1]))
# print(sum_lst)
# print(len(gp_point_lst))
# # print(len(sum_lst))
# print(sum_gp)
# print(sum_gp_point)
# print(result)

# # 25206 # 2

# std_dict = {}

# for i in range(20):
#     chihoon = list(map(str,input().split()))
#     std_dict[chihoon[0]] = [chihoon[2],chihoon[1]]

# grade_lst = list(std_dict.values())

# # 유효 성적 담을 리스트
# sum_lst = 0

# # 수강 학점의 합
# gp_point_lst = 0

# # 유효 성적 담기
# # 소수점 포함 숫자를 계산하기 위해서는 int()가 아닌 float()
# for s in grade_lst:
#     sub_point = float(s[1])

#     if s[0] == 'A+':
#         gp_point = 4.5
#         sum_lst += (gp_point * sub_point)
#         gp_point_lst += sub_point
#     elif s[0] == 'A0':
#         gp_point = 4.0
#         sum_lst += (gp_point* sub_point)
#         gp_point_lst += sub_point
#     elif s[0] == 'B+':
#         gp_point = 3.5
#         sum_lst += (gp_point* sub_point)
#         gp_point_lst += sub_point
#     elif s[0] == 'B0':
#         gp_point = 3.0
#         sum_lst += (gp_point* sub_point)
#         gp_point_lst += sub_point
#     elif s[0] == 'C+':
#         gp_point = 2.5
#         sum_lst += (gp_point* sub_point)
#         gp_point_lst += sub_point
#     elif s[0] == 'C0':
#         gp_point = 2.0
#         sum_lst += (gp_point* sub_point)
#         gp_point_lst += sub_point
#     elif s[0] == 'D+':
#         gp_point = 1.5
#         sum_lst += (gp_point* sub_point)
#         gp_point_lst += sub_point
#     elif s[0] == 'D0':
#         gp_point = 1.0
#         sum_lst += (gp_point* sub_point)
#         gp_point_lst += sub_point
#     elif s[0] == 'F':
#         gp_point = 0
#         sum_lst += (gp_point* sub_point)
#         gp_point_lst += sub_point
#     else:
#         pass   

# gp = sum_lst / gp_point_lst
# print(gp)