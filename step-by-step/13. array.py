# # 2750 수 정렬하기
# N = int(input())
# arr = []
# for _ in range(N):
#     n = int(input())
#     arr.append(n)

# for i in range(N-1, 0, -1):
#     for j in range(N-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] =  arr[j+1], arr[j]

# for num in arr:
#     print(num)


# # 대표값 2
# N = 5
# arr = []
# for _ in range(N):
#     n = int(input())
#     arr.append(n)

# for i in range(N-1, 0, -1):
#     for j in range(N-1):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] =  arr[j+1], arr[j]
# mid = arr[N//2]

# avrg = sum(arr)//N

# print(avrg)
# print(mid)



# # 25305 커트라인
# N, k = map(int, input().split())

# grade = list(map(int, input().split()))

# grade.sort(reverse=True)

# print(grade[k-1])


# 18870 좌표압축
N = int(input())