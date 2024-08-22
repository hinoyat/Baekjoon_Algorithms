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




# 28278 스택2
N = int(input())

def push():
    global stack

def poping():
    global stack
    

def cnt():
    global stack
    
def empty():
    global stack
    
def top():
    global stack
    
stack = []
for _ in range(N):
    order = input().split()
    print(order)

    if order[0] == '1':
        push(order[1])
    elif order[0] == '2':
        poping()
    elif order[0] == '3':
        cnt()
    elif order[0] == '4':
        empty()
    elif order[0] == '5':
        top()

