n, m, *A = map(int, open(0).read().split())
s = sum(A[:n])
for a in A[n:]:
    s *= not a or a
print(s)
