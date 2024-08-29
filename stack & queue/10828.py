# 스택

def push(command):
    global stack
    stack.append(command[1])

def pop():
    global stack
    if stack:
        a = stack.pop()
        print(a)
    else:
        print(-1)

def size():
    global stack
    return print(len(stack))
    
def empty():
    global stack
    if len(stack)==0:
        return print(1)
    else:
        return print(0)


def top():
    global stack
    if stack:
        return print(stack[-1])
    else:
        return print(-1)

N = int(input())
stack = []
for i in range(N):
    command = input().split()
    if command[0] == 'push':
        push(command)
    if command[0] == 'pop':
        pop()
    if command[0] == 'size':
        size()
    if command[0] == 'empty':
        empty()
    if command[0] == 'top':
        top()

# print(stack)