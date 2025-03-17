n, m, *A = map(int, open(0).read().split())
print("DOIUMTI"[sum(a - 1 for a in A) < m :: 2])
