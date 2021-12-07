n, m = map(int, input().split())


def f(x, f):
    y = 0
    while x//f:
        x, y = x//f, y+x//f
    return y


print(min(sum(s*f(i, j)
      for i, s in [(n, 1), (n-m, -1), (m, -1)]) for j in [2, 5]))
