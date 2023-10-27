n, m, *A = map(int, open(0).read().split()+[0])
x = 0
for i in range(n):
    x += A[i]+A[i-1] > m
    print(x)
