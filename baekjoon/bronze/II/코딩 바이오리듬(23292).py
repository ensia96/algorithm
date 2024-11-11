D, n, *A = open(0)
f = lambda a, b, c: sum((int(D[i]) - int(a[i])) ** 2 for i in range(b, c))
print(-max((f(a, 0, 4) * f(a, 4, 6) * f(a, 6, 8), -int(a)) for a in A)[1])
