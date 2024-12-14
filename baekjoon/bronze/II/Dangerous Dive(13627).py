n, r, *A = map(int, open(0).read().split())
print(*{*range(1, n + 1)} - set(A) or "*")
