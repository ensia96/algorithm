n = int(input())

for i in [*range(1, n)] + [*range(n, 0, -1)]:
    print(" " * (n - i) + "*" * (2 * i - 1))
