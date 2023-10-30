n, *A = map(int, open(0).read().split())
for i in range(n):
    A[i] == (n+1)*n/2-A[i] and exit(print(i+1))
