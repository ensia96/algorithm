*A, T = map(int, open(0).read().split())
q, T = divmod(T, sum(A))
C = []
for a in A:
    C += [(t := min(T, a)) + q * a]
    T -= t
a, b, c, d, e = C
print(d + e, c + e, a + -~b // 2)
