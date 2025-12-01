n, x, *A = map(int, open(0).read().split())
print(0 - max(x * n - sum(A), 0) // (x - 100))
