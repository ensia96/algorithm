n, m = map(int, input().split())
M = 500*n+1
C = [0]*M
N = [26*[-1]for _ in range(M)]
U = 1


def T(c): return ord(c)-ord('a')


def I():
    global U
    c = 0
    for s in input():
        t = T(s)
        if N[c][t] == -1:
            N[c][t] = U
            U += 1
        c = N[c][t]
    C[c] = 1


def F():
    c = 0
    for s in input():
        t = T(s)
        if N[c][t] == -1:
            return 0
        c = N[c][t]
    return C[c]


for _ in ' '*n:
    I()
print(sum(F()for _ in ' '*m))
