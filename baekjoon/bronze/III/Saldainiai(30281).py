n, *A = map(int, open(0).read().split())
s = sum(A)
print((max((s-a)*(a % 2)for a in A)if s % 2 else s)//2)
