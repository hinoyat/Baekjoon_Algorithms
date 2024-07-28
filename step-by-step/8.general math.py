# # 2745 진법 변환

# # n은 수 b는 진법 꼭 0도 포함 시키자
# num_lst = ['0','1','2','3','4','5','6','7','8','9']
# n, b = map(str,input().split())

# # print(ord('A')-55)


# result = []

# # 반복문 돌려서 리스트에 담기 숫자일땐 -49 알파벳은 -55
# for i in n:
#     if i in num_lst:
#         value = (ord(i) - 48)
#         result.append(value)
#     else:
#         value = (ord(i) - 55)
#         result.append(value)

# # 계산 저장할 변수 생성
# sum_value = 0

# # 반복문 돌며 진법 계산
# for s in range(len(result)):
#     check_value = result[s] * (int(b) ** (len(result)-s-1))
#     sum_value += check_value
# # print(result)
# print(sum_value)



# #11005  진법 변환 22

# # 알파벳의 진법 값 대문자로 주어짐
# # print(60466175 // 36, 60466175 % 36)
# # print(1679615 // 36, 1679615 % 36)
# # print(46655 // 36, 46655 % 36)
# # print(1295 // 36, 1295 % 36)
# # print(1295 // 36, 35 % 36)

# # print(754078538 // 36, 754078538 % 36)
# # print(20946626 // 36, 20946626 % 36)
# # print(581850 // 36, 581850 % 36)
# # print(16162 // 36, 16162 % 36)
# # print(448 // 36, 12 % 36)

# # num_value = chr(b) - 55

# #진법 변환하기2
# # for i in range(len(n),0,-1):



# n, b = map(int,input().split())
# # 찾으려는 값의 ord 값을 찾으려면 ord를 chr로 돌려줘야 함
# value = []


# while n >= 0:
#     if n > b:
#         s = n % b  # 35
#         n = n // b # 나눈 값을 다시 n에 할당
#         value.append(s)  #나머지 추가
#     elif n < b:   # b가 더 커지면 에러가 떠서 남은 n값 리스트에 추가

#         value.append(n)
#         break
#     else:
#         value.append(1)
#         value.append(0)
#         break
# print(value)
# result = []
# for i in range(len(value)):
#     if b == 10:
#         print(n)
#         break
#     if value[len(value)-1-i] >= 10:
#         result.append(chr(value[len(value)-1-i]+55))
#         print(result[i],end='')

#     else:
#         result.append(chr(value[len(value)-1-i]+48))
#         print(result[i],end='')

# #진법 변환하기2

# n, b = map(int,input().split())
# # 찾으려는 값의 ord 값을 찾으려면 ord를 chr로 돌려줘야 함
# value = []

# while n >= 0:
#     if n >= b:
#         s = n % b  # 35
#         n = n // b # 나눈 값을 다시 n에 할당
#         value.append(s)  #나머지 추가
#     if n < b:   # b가 더 커지면 에러가 떠서 남은 n값 리스트에 추가
#         value.append(n%b)
#         break


# result = []
# for i in range(len(value)):

#     if value[len(value)-1-i] >= 10:
#         result.append(chr(value[len(value)-1-i]+55))
#         print(result[i],end='')

#     else:
#         result.append(chr(value[len(value)-1-i]+48))
#         print(result[i],end='')