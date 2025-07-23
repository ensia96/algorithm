_, a, b, *A = map(int, open(0).read().split())
d, x, y = min((((x-a)**2+(y-b)**2)**.5, x, y)for x, y in zip(A[::2], A[1::2]))
print(a, b, x, y, f"{d:.2f}")
