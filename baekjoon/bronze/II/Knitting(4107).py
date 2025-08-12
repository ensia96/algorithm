*A, = open(0)
for l, p in zip(A[::2], A[1::2]):
    n, m, k = map(int, l.split())
    *p, = map(int, p.split())
    S = 0
    for i in range(m):
        S += n
        n += p[i % k]
    print(S)
