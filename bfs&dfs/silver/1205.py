# 등수 구하기

N, grade, P = map(int, input().split())

lst = list(map(int, input().split()))
print(lst)
lst.append(grade)
lst.sort(reverse=True)
dct = {}
