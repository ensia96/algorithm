M = 2**27
n = int(input())+1
N = range(1, n)
C = [[M]*n for _ in ' '*n]
R = [[0]*n for _ in ' '*n]
for _ in ' '*int(input()):
    a, b, c = map(int, input().split())
    C[a][b], R[a][b] = min(C[a][b], c), b
for k in N:
    C[k][k] = 0
    for i in N:
        for j in N:
            t = C[i][k]+C[k][j]
            if C[i][j] > t:
                C[i][j], R[i][j] = t, R[i][k]
for l in C[1:]:
    print(*l[1:])
for i in N:
    for j in N:
        if C[i][j] in [0, M]:
            print(0)
            continue
        r = [i]
        while r[-1] != j:
            r += R[r[-1]][j],
        print(len(r), *r)
