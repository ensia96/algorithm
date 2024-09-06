n, *A, x, y = map(int, open(0).read().split())
print(n * x // 100, sum(y <= a for a in A))
