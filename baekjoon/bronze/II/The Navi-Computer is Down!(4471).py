n, *A = open(0)
for i in range(int(n)):
    a, b, c = map(float, A[4*i+1].split())
    d, e, f = map(float, A[4*i+3].split())
    print(A[4*i][:-1], 'to', A[4*i+2][:-1], ((a-d)**2+(b-e)**2+(c-f)**2)**.5)
