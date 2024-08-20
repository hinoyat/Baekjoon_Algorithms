#큐

def push_back(command):
    global queue
    queue.append(command[1])

def pop_back():
    global queue
    if queue:
        a = queue.pop()
        print(a)
    else:
        print(-1)

def push_front(command):
    global queue
    queue.appendleft(command[1])

def pop_front():
    global queue
    if queue:
        a = queue.popleft()
        print(a)
    else:
        print(-1)

def size():
    global queue
    return print(len(queue))
    
def empty():
    global queue
    if len(queue)==0:
        return print(1)
    else:
        return print(0)

def front():
    global queue
    if queue:
        return print(queue[0])
    else:
        return print(-1)

def back():
    global queue
    if queue:
        return print(queue[-1])
    else:
        return print(-1)

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
queue = deque()
for i in range(N):
    command = input().split()
    if command[0] == 'push_back':
        push_back(command)
    if command[0] == 'pop_back':
        pop_back()
    if command[0] == 'push_front':
        push_front(command)
    if command[0] == 'pop_front':
        pop_front()
    if command[0] == 'size':
        size()
    if command[0] == 'empty':
        empty()
    if command[0] == 'front':
        front()
    if command[0] == 'back':
        back()