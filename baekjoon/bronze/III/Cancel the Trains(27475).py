_, *A = map(int, open(0).read().split())
while A:
    n, m, *A = A
    print(len({*A[:n]} & {*A[n:n+m]}))
    A = A[2+n+m:]
