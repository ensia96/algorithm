n, x, _, r, *A = map(int, open(0).read().split())
print(*map(sum, [*zip(*[(x - r < a < x + r, x - r == a or x + r == a) for a in A])]))
