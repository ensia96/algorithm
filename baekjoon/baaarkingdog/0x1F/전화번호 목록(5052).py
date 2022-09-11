for _ in ' '*int(input()):
    n = int(input())
    M = 10*n+1
    I, C, N = [], [0]*M, [10*[-1]for _ in ' '*M]
    A = U = 1
    for _ in ' '*n:
        c = 0
        I += input(),
        for s in I[-1]:
            t = int(s)
            if N[c][t] == -1:
                N[c][t] = U
                U += 1
            c = N[c][t]
        C[c] = 1
    for S in I:
        c = 0
        for s in S[:-1]:
            c = N[c][int(s)]
            if C[c]:
                A = 0
    print('YES'if A else'NO')
