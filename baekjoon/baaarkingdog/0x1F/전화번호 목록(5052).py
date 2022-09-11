for _ in ' '*int(input()):
    n = int(input())
    M = 10*n+1
    C, N = [0]*M, [10*[-1]for _ in ' '*M]
    A = U = 1
    for _ in ' '*n:
        c = 0
        for i in input():
            t = int(i)
            if N[c][t] == -1:
                N[c][t] = U
                U += 1
            c = N[c][t]
            if C[c]:
                A = 0
        C[c] = 1
    print('YES'if A else'NO')
