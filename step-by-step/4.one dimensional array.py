# # 10807

# n = int(input())
# num_list = list(map(int,input().split()))
# v = int(input())

# s=0
# for i in range(len(num_list)):
#     if num_list[i] == v:
#         s += 1
# print(s)

# # 10871

# n, x = map(int,input().split())
# num_list = list(map(int,input().split()))
# small_list = []

# for i in range(n):
#     if num_list[i] < x:
#         small_list.append(num_list[i])
# print(*small_list)

# # 10818
# import sys
# input = sys.stdin.readline
# n = int(input())
# num_list = list(map(int,input().split()))
# print(f'{min(num_list)} {max(num_list)}')



# # 2562

# a = 0
# num_list = []

# while a < 9:
#     number = int(input())
#     num_list.append(number)
#     a += 1
# for i in range(len(num_list)):
#     if max(num_list) == num_list[i]:
#         print(max(num_list))
#         print(i+1)


# #10810 공 넣기
# # N은 바구니 M은 앞으로 공을 넣을 횟수
# n, m = map(int, input().split())

# bag = [0]*n
# for s in range(m):
#     i, j, k = map(int, input().split())
#     for d in range(i,j+1):
#         bag[d-1] = f'{k}'
# for f in range(len(bag)):
#     print(bag[f],end=' ')



# # 10813 공 바꾸기

# n, m = map(int, input().split())
# bag = [0]*n
# for d in range(n):
#     bag[d] = d+1

# # print(bag)


# for s in range(m):
#     i, j = map(int, input().split())

#     bag_1 = bag[i-1]
#     bag_2 = bag[j-1]
#     bag[j-1] = bag_1
#     bag[i-1] = bag_2

#     # print(bag_1,bag_2)

# for f in range(len(bag)):
#     print(bag[f],end=' ')



# # 5597
# stu_num = 30
# student_list = []

# for i in range(stu_num):
#     student_list.append(i+1)

# for s in range(28):
#     good_student = int(input())
#     student_list.remove(good_student)


# for d in range(len(student_list)):
#     print(student_list[d])



# # 1546
# n = int(input())
# get_grade = list(map(int,input().split()))
# sorted_grade = sorted(get_grade)
# # print(sorted_grade)
# max = sorted_grade[len(get_grade)-1]
# # print(max)
# fake_grade_lst = []
# for i in sorted_grade:
#     new_grade = (i/max) * 100
#     fake_grade_lst.append(new_grade)
# sum_fake_grade = 0
# while len(fake_grade_lst) > 0:
#     s= fake_grade_lst.pop()
#     sum_fake_grade += s
# print(sum_fake_grade/len(get_grade))





# # 10811

# #  1   2   3   4   5   1  2
# # [0] [1] [2] [3] [4]  1->0  0 ->1
# #  2   1   3   4   5
# # [0] [1] [2] [3] [4]  3  4
# #  1   2   4   3   5
# # [0] [1] [2] [3] [4]  1  4
# #  3   4   2   1   5
# # [0] [1] [2] [3] [4]  2  2

# n, m = map(int,input().split())
# bucket = []
# for i in range(n):
#     bucket.append(i+1)

# for _ in range(m):
#     i, j = map(int,input().split())

#     bucket[i-1:j] = reversed(bucket[i-1:j])

# print(*bucket)


# # 개같이 멸망
# # for i in range(m):
# #     i, j = map(int,input().split())
# #     if i - 1 != 0:
# #         cng_bucket = bucket[j-1:i:-1] # [2, 1]
# #     else:
# #         cng_bucket = bucket[j-1::-1]
# #     cng_bucket_idx = 0
# #     for s in range(i, j):
# #         bucket[s-1:j-1] = cng_bucket[:]