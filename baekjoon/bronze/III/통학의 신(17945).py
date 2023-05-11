a, b = map(int, input().split())
print(*[sorted([*{-i, i-2*a}])
      for i in range(-1000, 1001)if i*(2*a-i) == b][-1])
