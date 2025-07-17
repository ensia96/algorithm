n, m, *A = map(int, open(0).read().split())
print(sum(a in A[n:]for a in A[:n]))
