N, M = map(int, input().split())
card = list(map(int, input().split()))
# for 문으로 부분집합 3장만 뽑으니 산관 없음
max_v = -0xffffffff
for i in range(N-2):
    for j in range(N-1):
        for s in range(N):
            if i < j and j < s:
                result = card[i] + card[j] + card[s]
                if result <= M:
                    if result > max_v:
                        max_v = result

print(max_v)


# 요것을 부분집합으로 풀기