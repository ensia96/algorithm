_, *A = map(int, open(i := 0).read().split())
while A:
    n, p, q, *A = A
    c = w = 0
    for a in sorted(A[:n]):
        if c < p and w+a < q:
            c += 1
            w += a
    i += 1
    A = A[n:]
    print(f"Case {i}:", c)
