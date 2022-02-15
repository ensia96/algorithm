def solution(n, info):
    M, S = {0: [-1]}, [(n, 0, [0]*11)]
    while S:
        c, d, A = S.pop()
        if d == 11 or not c:
            s, A[-1] = 0, c
            for i in range(11):
                if info[i] < A[i]:
                    s += 10-i
                if info[i] > A[i]:
                    s -= 10-i
            if s > 0:
                t = M.get(s, [0]*11)
                for i in range(11)[::-1]:
                    if A[i] > t[i]:
                        M[s] = A
                        break
                    if A[i] < t[i]:
                        break
            continue
        C = info[d]+1
        if c >= C:
            S += (c-C, d+1, [A[i] if i-d else C for i in range(11)]),
        S += (c, d+1, A),
    return M[max(M)]

# 신입 공채 당시에 제출했던 코드
#
# from itertools import combinations
#
#
# def can_win(data, info):
#     ryan = sum((data[i] > info[i])*(10-i) for i in range(10))
#     apeach = sum((info[i] > data[i])*(10-i) for i in range(10))
#     return ryan > apeach, ryan-apeach
#
#
# def solution(n, info):
#     d, ans, r = [info[i]+1 for i in range(10)], 0, []
#
#     for i in range(10):
#         for h in range(n-d[i]):
#             for data in combinations(filter(lambda x: x != i and d[i]+d[x] < n, range(10)), h):
#                 extra = n-d[i] - sum(map(lambda x: d[x], data))
#                 if 0 <= extra:
#                     dummy = [d[k]if k in [i]+[*data]else 0 for k in range(11)]
#                 dummy[10] = extra
#                 can, diff = can_win(dummy, info)
#                 if can and diff >= ans:
#                     r += [(diff, dummy)]
#                 ans = diff
#
#     dummy = [*filter(lambda x: x[0] == ans, r)]
#     answer = [-1]
#     if dummy:
#         answer = sorted(dummy, key=lambda x: x[1][::-1])[-1][1]
#     return answer
