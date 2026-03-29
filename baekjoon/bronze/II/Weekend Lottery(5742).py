n, *L = map(int, open(0).read().split())
while n:
    c, k, *L = L
    C = L[:n * c].count
    K = range(1, k + 1)
    print(*[k for k in K if C(k) == min(map(C, K))])
    n, *L = L[n * c:]
