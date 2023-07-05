n, *A = map(int, open(0).read().split())
x = sum(a*(a < 0)for a in A)
print((sum(A)-x)/(n+x))
