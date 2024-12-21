n, m = sorted(map(int, input().split()))
print([int((n * 2 + (n < m)) ** 0.5), "Impossible"][m < 1])
