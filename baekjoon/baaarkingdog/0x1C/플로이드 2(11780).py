import sys
I = sys.stdin.readline
M = 2**27
n = int(I())+1
N = range(1, n)
C = [[M]*n for _ in ' '*n]
R = [[0]*n for _ in ' '*n]
for _ in ' '*int(I()):
    a, b, c = map(int, I().split())
    C[a][b] = min(C[a][b], c)
for k in N:
    C[k][k] = 0
    for i in N:
        for j in N:
            t = C[i][k]+C[k][j]
            if C[i][j] > t:
                C[i][j], R[i][j] = t, k
for l in C[1:]:
    print(*(0 if i == M else i for i in l[1:]))


def f(i, j):
    if not R[i][j]:
        return []
    k = R[i][j]
    return f(i, k)+[k]+f(k, j)


for i in N:
    for j in N:
        if C[i][j] in [0, M]:
            print(0)
            continue
        r = [i]+f(i, j)+[j]
        print(len(r), *r)
