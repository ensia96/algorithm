*L, = open(0)
A = []
for X, Y in zip(L[2::3], L[3::3]):
    *X, = map(int, X.split())
    *Y, = map(int, Y.split())
    A += f'The maximum distance is {max(max(j - i, 0) * (Y[j] >= X[i])for i in range(len(X))for j in range(i, len(Y)))}',
print(*A, sep='\n\n')
