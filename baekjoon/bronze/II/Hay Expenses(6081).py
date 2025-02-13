n, q, *A = map(int, open(0).read().split())
for a, b in zip(A[n::2], A[n + 1 :: 2]):
    print(sum(A[a - 1 : b]))
