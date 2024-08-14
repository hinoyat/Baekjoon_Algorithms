result = 0
n = int(input())
if n == 1:
    result = 1
else:
    if n % 2 != 0:
        result = (n//2) * 3
    elif n % 2 == 0:
        result = (n//2)*3 -1
print(result)



n=int(input())
r=0
for i in range(1,n+1):
    for j in range(i,n//i+1):
        r+=1
print(r)