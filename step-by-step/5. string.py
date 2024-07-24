# #27866
# string = input()
# st_num = int(input())
# print(string[st_num-1])

# # 2743
# string = input()
# print(len(string))

# 9086
st_num = int(input())
fr_idx = 0
ls_num = st_num-1

for i in range(st_num):
    string = input()
    print(string[fr_idx],end='')
    print(string[ls_num])