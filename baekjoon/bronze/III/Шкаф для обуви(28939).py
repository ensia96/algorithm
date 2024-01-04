n, k, p, q, *A = map(int, open(0).read().split())
c = t = 0
for _ in ' '*n:
    x, y, *A = A
    t += sum(k*x < q*a or p*a < x for a in A[c:c+y+1])
    c += y
print(t)
