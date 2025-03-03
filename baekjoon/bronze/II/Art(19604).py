x = y = 100
X = Y = 0
for l in [*open(0)][1:]:
    a, b = map(int, l.split(","))
    x = min(x, a - 1)
    y = min(y, b - 1)
    X = max(X, a + 1)
    Y = max(Y, b + 1)
print(f"{x},{y}")
print(f"{X},{Y}")
