*A, = map(int, open(0).read().split())
while A:
    n, m, *A = A
    if n+m:
        T, A = A[:n-2], A[n-2:]
        print(*{*range(1, n+1)}-{*T, m})
