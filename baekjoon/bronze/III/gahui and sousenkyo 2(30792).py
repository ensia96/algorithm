_, *A = map(int, open(0).read().split())
print(sorted(A)[::-1].index(A[0])+1)
