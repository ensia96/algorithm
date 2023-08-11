n, *L = map(int, open(0).read().split())
A = L[:n]
for i in range(L[n]):
    a, b, c = L[i*3+n+1:i*3+n+4]
    if a < 2:
        for j in range(b-1, c):
            A[j] = A[j]**2 % 2010
    else:
        print(sum(A[b-1:c]))
