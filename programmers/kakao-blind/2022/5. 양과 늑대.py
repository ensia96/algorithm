def solution(info, edges):
    A, E = 0, [[] for i in range(len(info))]
    for i, j in edges:
        E[i] += j,

    S = [(1, 0, [0])]
    while S:
        s, w, v = S.pop()
        A = max(A, s)
        for p in v:
            for q in E[p]:
                if q in v:
                    continue
                t = info[q]
                a, b = s+(not t), w+t
                if a <= b:
                    continue
                S += (a, b, v+[q]),
    return A

# 5번은 트리관련 문제여서 그냥 무시함(잘 모름 ㅜㅠ)
