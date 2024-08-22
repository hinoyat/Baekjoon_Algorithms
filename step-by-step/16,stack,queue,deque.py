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
N = int(input())
lst = list(map(int, input().split()))

status = 'Nice'

first = 1
stack = []
min_pop = 21e8
pop_cnt = 0
poped = 0

while pop_cnt == N:

    if stack[-1] == first:
        stack.pop()

    # 순번 부르기
    poped = lst.pop(0)
    pop_cnt +=1
    
    # 세로 대기열 들어가는 사람이 먼저 들어간 사람보다 크면 break 
    if poped > min_pop:
        status = 'Sad'
        break
    else:
        min_pop = poped

        
    if poped == first:
        first += 1
    else:
        stack.append(poped)
print(status)