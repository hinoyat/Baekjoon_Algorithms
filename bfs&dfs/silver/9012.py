# 괄호

def check(lst):
    stack = []
    start = lst[0]
    if start == '(':
        stack.append(start)
    else:
        return 'NO'
    while stack:
        for i in range(1, len(lst)):
            if lst[i] == '(':
                stack.append(lst[i])
            elif lst[i] == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return 'NO'
                else:
                    return 'NO'
        if stack:
            return 'NO'
    if not stack:
        return 'YES'



N = int(input())

for _ in range(N):
    s = list(input())
    print(check(s))