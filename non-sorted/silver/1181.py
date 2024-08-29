# # 단어정렬
# import sys
# input = sys.stdin.readline
# N = int(input())
# seto = set()
# for i in range(N):
#     a = input().strip()
#     seto.add(a)
# lst = list(seto)
# lst.sort()
# lst.sort(key=len)

# for i in lst:
#     print(i)



# 10867 중복 빼고 정렬

N = int(input())
lst = list(map(int, input().split()))

lst = set(lst)
lst = list(lst)
lst.sort()
print(*lst)