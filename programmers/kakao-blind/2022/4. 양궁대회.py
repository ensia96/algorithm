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
