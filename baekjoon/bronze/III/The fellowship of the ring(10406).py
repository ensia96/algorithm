w, n, p, *A = map(int, open(0).read().split())
print(sum(w <= a <= n for a in A))
