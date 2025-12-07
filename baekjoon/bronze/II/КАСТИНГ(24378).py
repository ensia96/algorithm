x, n, *A = map(int, open(0).read().split())
print([0, max(sum(A) - 2 * n, 0), min(A)][x])
