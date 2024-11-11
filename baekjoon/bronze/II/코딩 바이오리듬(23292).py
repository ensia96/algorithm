D, n, *A = open(0)
print(
    -max((sum((int(D[i]) - int(a[i])) ** 2 for i in range(8)), -int(a)) for a in A)[1]
)
