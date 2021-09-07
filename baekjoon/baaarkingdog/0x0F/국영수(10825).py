i, t = input, int
print(*map(lambda x: x[0], sorted([i().split() for _ in range(t(i()))],
      key=lambda x: (-t(x[1]), t(x[2]), -t(x[3]), x[0]))))
