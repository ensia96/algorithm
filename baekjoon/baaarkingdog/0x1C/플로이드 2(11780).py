M = 2**27
n = int(input())
N = range(n)
C = [[M]*n for _ in ' '*n]
R = [[0]*n for _ in ' '*n]
for _ in ' '*int(input()):
    a, b, c = map(int, input().split())
    a, b = a-1, b-1
    C[a][b], R[a][b] = min(C[a][b], c), b
for k in N:
    C[k][k] = 0
    for i in N:
        for j in N:
            t = C[i][k]+C[k][j]
            if C[i][j] > t:
                C[i][j], R[i][j] = t, R[i][k]
for l in C:
    print(*l)
for i in N:
    for j in N:
        if i == j:
            print(0)
            continue
        r = [i+1]
        while r[-1]-1 != j:
            r += R[r[-1]-1][j]+1,
        print(len(r), *r)
