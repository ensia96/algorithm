f, r = lambda: [*map(int, input().split())], range
n, m = f()
T = [f()for _ in ' ' * n]
for _ in ' ' * m:
    g, x, y = f()
    print(sum((x + i, y + j) in T for i in r(g + 1)
          for j in r(g + 1 - i)if x + i + y + j <= g))
