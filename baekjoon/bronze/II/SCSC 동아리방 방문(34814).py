n, m, *A = map(int, open(0).read().split())
for l, h in zip(A[n::2], A[n + 1::2]):
    A[l - 1] -= max(A[:n]) > A[h - 1]
print(*A[:n])
