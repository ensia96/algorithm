n, f, *A = map(int, open(0).read().split())
A = [-((f-i)//-j)for i, j in zip(A[::2], A[1::2])]
print(A.index(min(A))+1)
