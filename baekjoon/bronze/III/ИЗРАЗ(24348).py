a, b, c = map(int, input().split())
print(max(max(x+y*z, x*y+z)for x, y,
      z in [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]))
