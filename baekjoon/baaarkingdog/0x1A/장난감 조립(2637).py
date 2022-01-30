l, A = lambda: map(int, input().split()), {}
n = next(l())
C, Q = [{}for _ in ' '*-~n], [(n, 1)]
for _ in ' '*next(l()):
    x, y, k = l()
    C[x][y] = k
for x, y in Q:
    if C[x]:
        for z, w in C[x].items():
            Q += (z, w*y),
    else:
        A[x] = A.get(x, 0)+y
for x, y in sorted(A.items()):
    print(x, y)
