# # 5086 배수와 약수
# a, b = map(int, input().split())
# while a !=0 and b !=0:

#     if a // b >0 and a % b == 0:
#         print('multiple')
#     elif b // a >0 and b % a == 0:
#         print('factor')
#     else:
#         print('neither')
#     a, b = map(int, input().split())


# # 2501 약수 구하기

# N, k = map(int, input().split())
# # 약수 셀겨
# cnt = 0
# # 그 숫자
# n = 1
# while True:
#     if N % n == 0:
#         cnt += 1
#         if cnt == k:
#             break
#     n += 1
#     if n > N:
#         break

# if cnt < k:
#     print(0)
# else:
#     print(n)


# # 9506 약수들의 합

# n = int(input())
# while n != -1:
#     lst = []
#     k = 1
#     while k<n:
#         if n % k ==0:
#             lst.append(k)
#         k += 1
#     if sum(lst) == n:
#         print(f'{n} = {" + ".join(map(str, lst))}')
#     else:
#         print(f'{n} is NOT perfect.')
#     n = int(input())
    
# # 2581 소수
# def prime(i):
#     if i<=1:
#         return False
#     if i <=3:
#         return True
#     if i%2 == 0 or i % 3 == 0:
#         return False
#     n = 5
#     while n*n <= i:
#         if i % n == 0 or i % (n+2) == 0:
#             return False
#         n += 6
#     return True
# start = int(input())
# end = int(input())

# lst = [i for i in range(start, end+1) if prime(i)]
# if len(lst) == 0:
#     print(-1)
# else:
#     print(sum(lst))
#     print(min(lst))