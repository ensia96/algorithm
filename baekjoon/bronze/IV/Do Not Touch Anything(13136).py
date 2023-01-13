r, c, n = map(int, input().split())
a, b = divmod(r, n)
x, y = divmod(c, n)
print((a+bool(b))*(x+bool(y)))
