# from collections import defaultdict
#
# def moving(cur, m, s, d):
#     i, j = cur
#     ni = (i + direction[d][0] * s) % N
#     nj = (j + direction[d][1] * s) % N
#     return (ni, nj)
#
#
# def boom(cur):
#     odd = False
#     even = False
#
#     # 질량의 합
#     sum_m = 0
#     # 속도의 합
#     sum_s = 0
#     # 개수
#     sum_cnt = 0
#
#     for nm, ns, nd in new_info[cur]:
#         # print(nm, ns, nd)
#         if nd % 2 == 0:
#             even = True
#         elif nd % 2 == 1:
#             odd = True
#         sum_m += nm
#         sum_s += ns
#         sum_cnt += 1
#     print(sum_m)
#     new_m = sum_m//5
#     print(new_m)
#     new_s = sum_s//sum_cnt
#     if new_m == 0:
#         print(new_m)
#         return []
#     if odd + even == 1:
#         nd1, nd2, nd3, nd4 = 1, 3, 5, 7
#     else:
#         nd1, nd2, nd3, nd4 = 0, 2, 4, 6
#
#     return [(new_m, new_s, nd1),(new_m, new_s, nd2),(new_m, new_s, nd3),(new_m, new_s, nd4)]
#
#
#
#
#
#
#
#
#
#
#
# N, M, K = map(int, input().split())
# arr = [[0] * N for _ in range(N)]
# # x, y, 질량, 속력, 방향
# # ri, ci, m, s, d
# direction = {
#     0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1),
#     4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)
# }
#
# info = defaultdict(list)
# for _ in range(M):
#     si, sj, m, s, d = map(int, input().split())
#     si -= 1
#     sj -= 1
#     info[(si, sj)].append((m, s, d))
#
#
# for _ in range(K):
#     new_info = defaultdict(list)
#     # 이동
#     print(info)
#     for key in info:
#         for now in info[key]:
#             # print(now)
#             m = now[0]
#             s = now[1]
#             d = now[2]
#             new_key = moving(key, m, s, d)
#             new_info[new_key].append((m, s, d))
#     print(new_info)
#
#     # 퍼트리기
#     for new_key2 in new_info:
#         print(new_info[new_key2])
#         if len(new_info[new_key2]) > 1:
#             new_val = boom(new_key2)
#             new_info[new_key2] = new_val
#
#     # 여기서 체크
#     info = new_info
# print(info, '퍼트리고 난 후')
# total_mass = sum(m for fireballs in info.values() for m, _, _ in fireballs)
# print(total_mass)
#
#
#
# from collections import defaultdict
#
#
# def moving(cur, s, d):
#     i, j = cur
#     ni = (i + direction[d][0] * s) % N
#     nj = (j + direction[d][1] * s) % N
#     return (ni, nj)
#
#
# def boom(fireballs):
#     odd = even = False
#     sum_m = sum_s = sum_cnt = 0
#
#     for m, s, d in fireballs:
#         odd |= d % 2 == 1
#         even |= d % 2 == 0
#         sum_m += m
#         sum_s += s
#         sum_cnt += 1
#
#     new_m = sum_m // 5
#     if new_m == 0:
#         return []
#
#     new_s = sum_s // sum_cnt
#     new_d = [0, 2, 4, 6] if odd != even else [1, 3, 5, 7]
#
#     return [(new_m, new_s, d) for d in new_d]
#
#
# N, M, K = map(int, input().split())
#
# direction = {
#     0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1),
#     4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)
# }
#
# info = defaultdict(list)
# for _ in range(M):
#     si, sj, m, s, d = map(int, input().split())
#     info[(si - 1, sj - 1)].append((m, s, d))
#
# for _ in range(K):
#     new_info = defaultdict(list)
#
#
#     for key, fireballs in info.items():
#         for m, s, d in fireballs:
#             new_key = moving(key, s, d)
#             new_info[new_key].append((m, s, d))
#
#
#     for key, fireballs in new_info.items():
#         if len(fireballs) > 1:
#             new_info[key] = boom(fireballs)
#
#     info = new_info
# print(info)
#
# # Calculate total mass
# # total_mass = sum(m for fireballs in info.values() for m, _, _ in fireballs)
# # print(total_mass)


from collections import defaultdict


def moving(cur, m, s, d):
    i, j = cur
    ni = (i + direction[d][0] * s) % N
    nj = (j + direction[d][1] * s) % N
    return (ni, nj)


def boom(cur):
    odd = False
    even = False

    sum_m = 0
    sum_s = 0
    sum_cnt = 0

    for nm, ns, nd in new_info[cur]:
        if nd % 2 == 0:
            even = True
        else:
            odd = True
        sum_m += nm
        sum_s += ns
        sum_cnt += 1

    new_m = sum_m // 5
    new_s = sum_s // sum_cnt
    if new_m == 0:
        return []
    if odd + even == 1:
        nd1, nd2, nd3, nd4 = 0, 2, 4, 6
    else:
        nd1, nd2, nd3, nd4 = 1, 3, 5, 7

    return [(new_m, new_s, nd1), (new_m, new_s, nd2), (new_m, new_s, nd3), (new_m, new_s, nd4)]


N, M, K = map(int, input().split())

direction = {
    0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1),
    4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)
}

info = defaultdict(list)
for _ in range(M):
    si, sj, m, s, d = map(int, input().split())
    si -= 1
    sj -= 1
    info[(si, sj)].append((m, s, d))

for _ in range(K):
    new_info = defaultdict(list)
    # 이동
    for key in info:
        for now in info[key]:
            m, s, d = now
            new_key = moving(key, m, s, d)
            new_info[new_key].append((m, s, d))

    # 퍼트리기
    for new_key in new_info:
        if len(new_info[new_key]) > 1:
            new_val = boom(new_key)
            new_info[new_key] = new_val

    info = new_info

# 최종 결과 계산
total_mass = 0
for fireballs in info.values():
    for fireball in fireballs:
        mass = fireball[0]
        total_mass += mass

print(total_mass)
