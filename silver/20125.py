from pprint import pprint as pppp
N = int(input())
arr = [input() for _ in range(N)]
# pppp(arr)
heart = []
find_heart = 0
for i in range(N):
    for j in range(N):
        if find_heart == 0:
            if arr[i][j] == '*':
                heart = [i+1, j]
                find_heart += 1
                break

hi, hj = heart

left_arm = arr[hi][0:hj].count('*')
right_arm = arr[hi][hj+1:N].count('*')

body = 0
for i in range(hi+1, N):
    if arr[i][hj] == '*':
        body += 1

left_leg = 0
right_leg = 0
for i in range(hi+1, N):
    if arr[i][hj-1] == '*':
        left_leg += 1
    if arr[i][hj+1] == '*':
        right_leg += 1
print(hi+1, hj+1)
print(left_arm, right_arm, body, left_leg, right_leg)