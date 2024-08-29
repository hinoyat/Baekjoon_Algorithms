T = int(input())

winner = ''

while True:
    if T > 1:
        T -= 1
        if T == 1:
            winner = 'CY'
            break
        T -= 1
        if T == 1:
            winner = 'SK'
            break
    else:
        winner = 'SK'
        break
print(winner)