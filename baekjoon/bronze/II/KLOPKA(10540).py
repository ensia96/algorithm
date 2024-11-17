(*A,) = map(int, open(0).read().split()[1:])
print((max(A) - min(A)) ** 2)
