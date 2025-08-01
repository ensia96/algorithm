*A, = map(int, open(0).read().split())
for n, k in zip(A[1::2], A[2::2]):
    print((n-k)//~-k)
