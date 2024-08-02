from pprint import pprint

#2669 직사각형 네개의 합집합의 면적 구하기

# 면적의 최대

arr_len = 100
arr = [[0 for _ in range(arr_len)]for _ in range(arr_len)]

# 정수를 몇 번 입력하는지
test = 4

# test 동안 사각형 입력
for tc in range(test):
    co_lst = list(map(int,input().split()))
    # [x1, y1, x2, y2]
    # [1 , 2 , 3 , 4 ]
    
    for i in range(co_lst[0], co_lst[2]):
        for j in range(co_lst[1], co_lst[3]):
            arr[j][i] = 1
    # print(co_lst)
    # co_lst.clear()  필요할 줄 알았는데 for문 돌 때마다 갱신되는 것을 알았습니다.

# pprint(arr)

# 면적의 합
sum = 0

# 2차원 배의 행을 하나씩 뜯어서
for s in arr:
    #하나씩 1인지 더했어요!
    for i in range(arr_len):
        if s[i] == 1:
            sum += 1

print(sum)