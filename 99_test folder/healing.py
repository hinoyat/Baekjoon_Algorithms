import sys

sys.setrecursionlimit(100000)


def right_up(i, j, cnt):
    if cnt == move:
        return i, j, cnt

    if i == row and j == col:
        return left_down(i, j, cnt)

    elif i == row and j < col:
        return right_down(i, j, cnt)

    elif 0 < i < row and j == col:
        return left_up(i, j, cnt)
    cnt += 1
    i += 1
    j += 1
    # print(0)
    # print(i, j, cnt)
    return right_up(i, j, cnt)


def left_up(i, j, cnt):
    if cnt == move:
        return i, j, cnt

    if i == row and 0 < j < col:
        return left_down(i, j, cnt)

    elif i == row and j == 0:
        return right_down(i, j, cnt)

    elif i < row and j == 0:
        return right_up(i, j, cnt)
    cnt += 1
    i += 1
    j -= 1
    # print(1)
    # print(i, j, cnt)
    return left_up(i, j, cnt)


def left_down(i, j, cnt):
    if cnt == move:
        return i, j, cnt

    if i == 0 and 0 < j < col:
        return left_up(i, j, cnt)

    elif i == 0 and j == 0:
        return right_up(i, j, cnt)

    elif 0 < i < row and j == 0:
        return right_down(i, j, cnt)
    cnt += 1
    i -= 1
    j -= 1
    # print(3)
    # print(i, j, cnt)
    return left_down(i, j, cnt)


def right_down(i, j, cnt):
    if cnt == move:
        return i, j, cnt

    if 0 < i < row and j == col:
        return left_down(i, j, cnt)

    elif i == 0 and j == col:
        return left_up(i, j, cnt)

    elif i == 0 and 0 < j < col:
        return right_up(i, j, cnt)
    cnt += 1
    i -= 1
    j += 1
    # print(4)
    # print(i, j, cnt)
    return right_down(i, j, cnt)


col, row = map(int, input().split())
s_j, s_i = map(int, input().split())
move = int(input())
# arr = [[0 for _ in range(col)] for _ in range(row)]
cnt_v = 0
result = right_up(s_i, s_j, cnt_v)
# print(result)
end_i = result[1]
end_j = result[0]
print(end_i, end_j)
# pprint(arr)