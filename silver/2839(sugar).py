N = int(input())
a = 3
b = 5
min_v = 50000

i = 0
if N >= b:
    if N%b == 0:
        min_v = N//b
    else:
        while b * i <= N:
            s = N - b*i
            v = 0
            if s >= a:
                if s % a ==0:
                    v = i + s//a
                    if v < min_v:
                        min_v = v
            elif s < a:
                if min_v == 50000:
                    min_v = -1
            i += 1
            
else:
    if N >= a:
        if N % a == 0:
            min_v = N//a
        else:
            min_v = -1
    else:
        min_v = -1
print(min_v)