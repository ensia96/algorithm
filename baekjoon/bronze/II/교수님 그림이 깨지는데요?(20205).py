n, k, *A = map(int, open(0).read().split())
for i in range(n):
    for _ in ' '*k:
        print(*[A[i*n+j//k]for j in range(k*n)])
