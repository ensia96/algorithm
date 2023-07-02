n, s, *M = map(int, open(0).read().split())
x, y = divmod(max(M)*s, 1000)
print(x+bool(y))
