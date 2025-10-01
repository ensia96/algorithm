a, b, c, n = map(int, open(0).read().split())
print(n * c + n // 2 * b + n % 2 * (a + b))
