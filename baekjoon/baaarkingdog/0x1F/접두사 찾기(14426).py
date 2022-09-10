n, m = map(int, input().split())
M = n*500+1
C = [0]*M
N = [26*[-1]for _ in ' '*M]
U = 1
A = 0
for _ in ' '*n:
    c = 0
    for s in input():
        t = ord(s)-ord('a')
        if N[c][t] == -1:
            N[c][t] = U
            U += 1
        c = N[c][t]
    C[c] = 1
for _ in ' '*m:
    c = 0
    for s in input():
        t = ord(s)-ord('a')
        if N[c][t] == -1:
            break
        c = N[c][t]
    else:
        A += 1
print(A)
