n, x, *A = map(int, open(0).read().split())
print(max(0, -(((x * n) - sum(A)) // (x - 100))))
