n, k, p, *A = map(int, open(0).read().split())
print(sum(sum(A[i*k:-~i*k]) > k-p for i in range(n)))
