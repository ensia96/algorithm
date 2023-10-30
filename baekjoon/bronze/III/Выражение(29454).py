n, *A = map(int, open(0).read().split())
for i in range(n):
    A[i] == sum(A)-A[i] and exit(print(i+1))
