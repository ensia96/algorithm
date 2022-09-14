n = int(input())
M = 10*n+1
C = [0]*M
N = [26*[-1]for _ in ' '*M]
U = 1
for _ in ' '*n:
    c, f, A = 0, 1, ''
    for s in input():
        t = ord(s)-ord('a')
        A += s*f
        if N[c][t] == -1:
            N[c][t], f = U, 0
            U += 1
        c = N[c][t]
    C[c] += 1
    print(A+str(C[c])*(C[c] > 1))
