a, m, n = map(int, open(0).read().split())
print(min(max(x := m / a, n), max(y := n / a, m), 2 * x, 2 * y))
