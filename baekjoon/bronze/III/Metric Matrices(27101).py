n, *A = map(int, open(0).read().split())
N = range(n)
for i in N:
    A[i*n+i] and exit(print(0))
for i in N:
    for j in N:
        i != j and A[i*n+j] < 1 and exit(print(2))
for i in N:
    for j in N:
        A[i*n+j] != A[j*n+i] and exit(print(3))
for i in N:
    for j in N:
        for k in N:
            A[i*n+j]+A[j*n+k] < A[i*n+k] and exit(print(4))
print(0)
