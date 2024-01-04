n, k, p, q, *A = map(int, open(0).read().split())
t = 0
for _ in ' '*n:
    x, y, *A = A
    A, B = A[y:], A[:y]
    t += sum(k*x < q*b or p*b < x for b in B)
print(t)
