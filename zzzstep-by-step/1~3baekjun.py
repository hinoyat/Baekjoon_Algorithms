# 18108
# a = int(input())
# print(a-543)

# 10430
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

# #10430
# a, b, c = map(int, input().split())
# print((a + b) % c)
# print(((a % c) + (b % c)) % c)
# print((a * b) % c)
# print(((a % c) * (b % c)) % c)

# #2588
#
# a = int(input())
# b = (input())
#
# units = int(b[2])
# tens = int(b[1])
# hundreds = int(b[0])
#
# print(a*units)
# print(a*tens)
# print(a*hundreds)
# print(a*int(b))

# #11382
# a, b, c = map(int, input().split())
# print(a+b+c)

# #10171
# print("\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")

# #10172
# print("|\\_/|")
# print("|q p|   /}")
# print('( 0 )\"\"\"\\')
# print("|\"^\"`    |")
# print('||_/=\\\\__|')

# #1330
# a, b = map(int, input().split())
# if a>b:
#     print(">")
# elif a<b:
#     print("<")
# else:
#     print("==")

# #9498
# a = input()

# if int(a)>=90:
#     print("A")
# elif int(a)>=80:
#     print("B")
# elif int(a)>=70:
#     print("C")
# elif int(a)>=60:
#     print("D")
# else:
#     print("F")

# #2753
# a = input()
# if int(a) % 4 == 0 and int(a) % 100 != 0: 
#     print("1")
# elif int(a) % 400 == 0:
#     print("1")
# else:
#     print("0")


# a = input()
# if (int(a) % 4 == 0 and int(a) % 100 !=0) or (int(a) % 400 == 0):
#     print("1")
# else:
#     print("0")

# #14681

# a = input()
# b = input()

# if int(a) > 0 and int(b) > 0:
#     print("1")
# elif int(a) < 0 and int(b) > 0:
#     print("2")
# elif int(a) < 0 and int(b) < 0:
#     print("3")
# elif int(a) > 0 and int(b) < 0:
#     print("4")

# #2884

# h, m = map(int, input().split())
# chang = ((h*60)+m)-45
# hour = (chang//60)
# min = (chang%60)

# if hour <0:
#     print(24+hour, min)
# else:
#     print(hour, min)


## 2739
# list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = input()
# for i in list_a:
#     print(f"{n} * {i} =",int(n)*i)

# n = int(input())
# for i in range(0,10):
#     print(f"{n} * {i} =",n*i)

# #10950
# #while문
# T = int(input())
# a, b = list(map(int,input().split()))
# s = 1
# print(a+b)

# while s < T :
#     a, b = list(map(int,input().split()))
#     print(a+b)
#     s += 1

#for문

# T = int(input())
# for i in range(0,T):
#     a, b = list(map(int,input().split()))
#     print(a+b)

# #8393
# n = int(input())
# start = 0
# sum = 0
# while start < n:
#     start += 1
#     sum += start
# print(sum)


# #25304
# X = int(input())
# N = int(input())

# start_count = 0
# x_count = 0
# input_price = 0
# final_price = 0

# while start_count != N:
#     input_price, x_count = list(map(int,input().split()))
#     final_price += (input_price * x_count)
#     start_count += 1
# if final_price == X:
#     print('Yes')
# else:
#     print('No')

# #25314
# N = int(input())
# count=0
# for i in range(0,N,4):
#     count += 1
# print('long '*(count-1)+'long','int')


# #15552
# import sys
# T = int(input())
# input = sys.stdin.readline #lambda: sys.stdin.readline().rstrip() 이거 모임
# result = [] # result를 저장하기 위한 빈 방을 만든 것
# for i in range(0,T):
#     A, B = list(map(int,input().split()))
#     result.append(A+B) #append는 리스트에 추가할 때 사용됨
# print(*result) # *을 붙이면 결과가 리스트 말고 걍 쭈르르르 나옴

# #11021
# import sys
# T = int(input())
# input = sys.stdin.readline
# for i in range(0,T):
#     A, B = list(map(int,input().split()))
#     print(f'Case #{i+1}:', A+B)

# #11021
# import sys
# T = int(input())
# input = sys.stdin.readline
# for i in range(0,T):
#     A, B = list(map(int,input().split()))
#     print(f'Case #{i+1}: {A} + {B} =', A+B)


# #2439
# N=int(input())

# for i in range(0,N):
#     print(' '*(N-(i+1))+'*'*(i+1))

# test
import sys
input = sys.stdin.readline
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 오름차순으로 정렬하면서, 중간에 배열 A가 배열 B와 같은지 확인
for i in range(N-1, 0, -1):
    max_idx = 0
    
    # 최대값을 찾아서 맨 뒤로 이동
    for j in range(1, i + 1):
        if A[j] > A[max_idx]:
            max_idx = j

    A[i], A[max_idx] = A[max_idx], A[i]

    # 배열 A와 배열 B를 비교
    if A == B:
        print(1)
        break
else:
    print(0)
