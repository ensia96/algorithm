n, *A, t, p = map(int, open(0).read().split())
z = 0
for a in A:
    x, y = divmod(a, t)
    z += x+bool(y)
print(z)
print(*divmod(n, p))
