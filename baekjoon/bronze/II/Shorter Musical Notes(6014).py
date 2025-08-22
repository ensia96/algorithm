n, q, *L = map(int, open(0).read().split())
A = []
for i in range(n):
    A += [i]*L[i]
for l in L[n:]:
    print(A[l]+1)
