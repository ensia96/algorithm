_, *A = map(int, open(0).read().split())
while A:
    m, n, *A = A
    A = A[m+n:]
    print(1+6*(m*n > 3))
