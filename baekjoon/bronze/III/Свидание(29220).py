k, n, *A = map(int, open(0).read().split())
s = sum(A)
print('YNEOS'[all(s-a < k for a in A)::2])
