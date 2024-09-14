n, m, *A = map(int, open(0).read().split())
for i in range(1, m + 1):
    for j in range(n - 1):
        if A[j] % i > A[j + 1] % i:
            A[j], A[j + 1] = A[j + 1], A[j]
[*map(print, A)]
