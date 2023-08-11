n, *C = open(0).read().split()
n = int(n)
*A, = map(int, C[:n+n])
for i in range(n):
    for j in range(i, n):
        if A[i]-A[j] <= A[n+i]+A[n+j] and C[n+n+i] != C[n+n+j]:
            print('YES')
            exit(print(i+1, j+1))
print('NO')
