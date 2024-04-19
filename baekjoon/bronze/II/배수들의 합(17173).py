n, m, *A = map(int, open(0).read().split())
print(sum(i*any(i % a == 0 for a in A)for i in range(1, n+1)))
