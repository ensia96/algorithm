n, m, *A = map(int, open(0).read().split())
print(max(A.count(a)for a in A))
