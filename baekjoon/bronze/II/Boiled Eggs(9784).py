_, *A = map(int, open(i := 0).read().split())
while A:
    n, p, q, *A = A
    w = 0
    print(f"Case {i}:", min(p, sum([q >= (w := w+a)for a in sorted(A[:n])])))
    i += 1
    A = A[n:]
