N = int(input())
chat_log = [input() for _ in range(N)]
newbie = 'ENTER'
# print(chat_log)

gom_cnt = 0
gom_log = set()
chat = 1
while chat < N:
    if chat_log[chat] == newbie:
        gom_cnt += len(gom_log)
        gom_log = set()
    else:
        gom_log.add(chat_log[chat]) 
    # print(chat_log[chat])
    # print(gom_log)
    
    chat += 1
if gom_log:
    gom_cnt += len(gom_log)
print(gom_cnt)