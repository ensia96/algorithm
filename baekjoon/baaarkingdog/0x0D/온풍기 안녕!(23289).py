L, R = lambda: map(int, input().split()), range
n, m, k = L()
A, B = lambda i, j: 0 <= i < n and 0 <= j < m, [[0]*m for _ in ' '*n]
W = {(p//m, p % m): [1]*4 for p in R(n*m)}
D, I = lambda i, j: [(i, j+1), (i, j-1), (i-1, j), (i+1, j)], {}
H = [(i, j)for i in R(n)for j in R(m)]
Z = [(i, j) for i, j in H if not (0 < i < n-1 and 0 < j < m-1)]

for i in R(n):
    t = [*L()]
    for j in R(m):
        if t[j]:
            I[t[j]-1] = I.get(t[j]-1, [])+[(i, j)]

for _ in ' '*next(L()):
    x, y, t = L()
    x, y, T = x-1, y-1, not t
    W[(x, y)][T*2] = W[(x-T, y+t)][T*2+1] = 0


def w(i, j, x):
    Q = [(5, i, j)]
    V = [[0]*m for _ in ' '*n]
    V[i][j] = 1
    for d, i, j in Q:
        B[i][j] += d
        if d < 2:
            continue
        P = D(i, j)
        O = [[(P[2], i-1, j+1, (0, 3)), (P[3], i+1, j+1, (0, 2))], [(P[2], i-1, j-1, (1, 3)), (P[3], i+1, j-1, (1, 2))],
             [(P[1], i-1, j-1, (0, 2)), (P[0], i-1, j+1, (1, 2))], [(P[1], i+1, j-1, (0, 3)), (P[0], i+1, j+1, (1, 3))]][x]
        for K, p, q, H in [((i, j), *P[x], (x,))]+O:
            if A(*K)*A(p, q) and all(W[(*K,)][h]for h in H) and not V[p][q]:
                V[p][q] = 1
                Q += (d-1, p, q),


def t():
    O = [[0]*m for _ in ' '*n]
    for i, j in H:
        if not B[i][j]:
            continue
        T = D(i, j)
        for k in R(4):
            p, q = T[k]
            if A(p, q) and W[(i, j)][k]*(B[i][j] > B[p][q]):
                h = (B[i][j]-B[p][q])//4
                O[i][j] -= h
                O[p][q] += h
    for i, j in H:
        B[i][j] += O[i][j]


for a in R(102):
    if all(B[i][j] >= k for i, j in I[4]):
        break
    for x in R(4):
        for i, j in I.get(x, []):
            p, q = D(i, j)[x]
            A(p, q) and w(p, q, x)
    t()
    for i, j in Z:
        B[i][j] -= bool(B[i][j])
print(a)
