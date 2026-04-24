x, n, *A = map(int, open(0).read().split())
print([max(sum(A) - 2 * n, 0), min(A)][x - 1])
