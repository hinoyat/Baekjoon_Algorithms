# 요세푸스 문제

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
# print(lst)

stack = []
start = lst.pop(M-1)
stack.append(start)

# 제거 순번 카운트
cnt = 0
# 인덱스 계산
idx = M-2
while lst:
    
    if cnt == M:
        y = lst.pop(idx)
        stack.append(y)
        cnt = 0
        idx -=1
    
    idx += 1
    if idx >= len(lst):
        idx = 0
    cnt += 1

print(f'<{", ".join(map(str, stack))}>')