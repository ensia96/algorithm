a, b = map(int, open(0))
x, a = divmod(a, 3)
y, b = divmod(b, 3)
print(*[[-1], [x, a, y]][a == b])
