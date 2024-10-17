n, h, *A = map(int, open(0).read().split())
print(min([i + 1 for i in range(n) if (x := sum(A[: i + 1])) >= h] or [-1]))
