n, k, *A = map(int, open(0).read().split())
print(sum(k == A[i] + A[j] for i in range(n) for j in range(i + 1, n)))
