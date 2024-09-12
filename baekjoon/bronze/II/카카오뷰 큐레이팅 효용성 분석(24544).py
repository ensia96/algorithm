n, *A = map(int, open(0).read().split())
print(sum(A[:n]))
print(sum(A[i] * (1 ^ A[i + n]) for i in range(n)))
