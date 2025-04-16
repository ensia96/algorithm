l, c, n, *A = map(int, open(0).read().split())
for a, b in zip(A[::2], A[1::2]):
    print(abs(n-b)+a)
