_, *A = map(int, open(0).read().split())
while A:
    n, m, *A = A
    A = A[m+n:]
    print('YNeos'[n > m::2])
