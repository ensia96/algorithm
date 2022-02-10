n = int(input())
N = n**2
f, D = lambda x: 0 <= x < n, [[0]*n for i in ' '*n]
g, F = lambda i, j: [(i+1, j), (i-1, j), (i, j+1), (i, j-1)], {}
C = [(i, j)for i in range(n)for j in range(n)]
for _ in ' '*N:
    s, *L = map(int, input().split())
    F[s], A = L, []
    for i, j in C:
        if D[i][j]:
            continue
        a = b = 0
        for x, y in g(i, j):
            if f(x)*f(y):
                a += D[x][y] in Lb += not D[x][y]
        A += (-a, -b, i, j),
    a, b, c, d = sorted(A)[0]
    D[c][d] = s
A = 0
for i, j in C:
    a = sum(D[x][y] in F[D[i][j]]for x, y in g(i, j)if f(x)*f(y))
    if a:
        A += 10**~-a
print(A)
