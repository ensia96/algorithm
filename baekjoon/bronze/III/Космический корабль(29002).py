n, *A = map(int, open(0).read().split())
s = sum(A)
print(*[a for a in A if s != 2*a], s//2)
