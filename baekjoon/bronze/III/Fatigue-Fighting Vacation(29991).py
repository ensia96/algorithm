d, c, r, *A = map(int, open(0).read().split())
A, B = A[:c], A[c:]
c = 0
for a in A:
    while d < a and B:
        b, *B = B
        c += 1
        d += b
    d -= a
    c += d >= 0
print(c)
