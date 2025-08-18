n, *L = map(int, open(0).read().split())
A = [*range(n+1)]
for x, y in zip(L[1::2], L[2::2]):
    A[x] = y
print(*A[1:])
