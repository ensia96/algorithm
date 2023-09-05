n, *A = map(int, open(0).read().split())
print(sum(3*(a > b)+(a == b)for a, b in zip(A[:n], A[n:])))
