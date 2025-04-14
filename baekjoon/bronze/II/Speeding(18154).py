a, x, y, *A = map(int, open(t := 0).read().split())
for a, b in zip(A[::2], A[1::2]):
    t = max(t, (y - b) // (x - a))
    x, y = a, b
print(t)
