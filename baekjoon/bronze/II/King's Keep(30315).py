n, *L = map(int, open(0).read().split())
print(min(sum(((L[2 * i] - L[2 * j])**2 + (L[2 * i + 1] - L[2 * j + 1])
      ** 2)**0.5 for i in range(n)) / ~-n for j in range(n)))
