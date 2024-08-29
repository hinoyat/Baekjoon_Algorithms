# # 10773 제로
# import sys
# input = sys.stdin.readline
# N = int(input())
# stack = []
# for _ in range(N):
#     a = int(input())
#     if a != 0:
#         stack.append(a)
#     else:
#         stack.pop()
# print(sum(stack))




# # 28278 스택2

# def push(v):
#     global stack
#     stack.append(v)

# def poping():
#     global stack
#     if stack:
#         v = stack.pop()
#         return v
#     else:
#         return -1

# def cnt():
#     global stack
#     return len(stack)

# def empty():
#     global stack
#     if stack:
#         return 0
#     else:
#         return 1

# def top():
#     global stack
#     if stack:
#         return stack[-1]
#     else:
#         return -1

# import sys
# input = sys.stdin.readline
# N = int(input())
# stack = []
# for _ in range(N):
#     order = input().split()

#     if order[0] == '1':
#         push(order[1])

#     elif order[0] == '2':
#         rst = poping()
#         print(rst)

#     elif order[0] == '3':
#         rst = cnt()
#         print(rst)

#     elif order[0] == '4':
#         rst = empty()
#         print(rst)
#     elif order[0] == '5':
#         rst = top()
#         print(rst)



# # 균형잡힌 세상
# def balance(word):
#     stack = []
#     for i in word:
#         if i =='(':
#             stack.append(i)
#         elif i == '[':
#             stack.append(i)
#         elif i == ')':
#             if stack:
#                 m = stack.pop()
#                 if m != '(':
#                     return 'no'
#             else:
#                 return 'no'
#         elif i == ']':
#             if stack:
#                 m = stack.pop()
#                 if m !='[':
#                     return 'no'
                
#             else:
#                 return 'no'
#     if stack:
#         return 'no'
#     else:
#         return 'yes'
                    


# n = input()
# while n != '.':
#     r = balance(n)
#     print(r)
#     n = input()



# 12789 도키도키 간식드리미
def dokidoki(lst):
    status = 'Nice'
    # 받은 사람이 들어간다
    result = []
    # 대기소
    stack = []
    # 번호표
    num = 1
    # 최솟값 구하면서 더 큰 값 대기열에 오면 sad ㅠㅠ
    min_v = 21e8

    while lst:
        n = lst.pop(0)
        # 스택에 없을 때
        if n > num:
            # if min_v<n:
            #     status = 'Sad'
            #     break
            # else:
            min_v = n
            stack.append(n)
        elif n == num:
            result.append(n)
            num+=1

        # 스택에 있을 때
        if stack and lst:
            if stack[-1] == num:
                a = stack.pop()
                result.append(a)
                num += 1
            elif lst[0] == num:
                a = lst.pop(0)
                result.append(a)
                num += 1






N = int(input())
lst = list(map(int, input().split()))





    
    
print(stack)
print(status)