n, p, q, *A = map(int, open(0).read().split())
C = []
for a, b in zip(A[:n], A[n:]):
    c = 0
    while a != b:
        a += p
        b += q
        c += 1
        c == 1e4 and exit(print("NO"))
    C += (c,)
print("YES")
print(*C)
