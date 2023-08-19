n, *A = map(int, open(0).read().split())
for i in range(n)[::-1]:
    a, *A = A
    T, A = A[:2*a], A[2*a:]
    X, Y = T[::2], T[1::2]
    R = range(a)
    print(f'Case #{n-i}:', sum((X[j] < X[k] and Y[j] > Y[k]) +
          (X[j] > X[k] and Y[j] < Y[k])for j in R for k in R)//2)
