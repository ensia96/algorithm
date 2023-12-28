d, c, r, *A = map(int, open(0).read().split())
d += sum(A[c:])
for a in A:
    d -= a
    r += d >= 0
print(r)
