L, A = lambda: map(int, input().split()), 0
n = next(L())
R, P = [*L()], [*L()]
x = P[0]
for i in range(n-1):
    A += R[i]*x
    x = min(x, P[i+1])
print(A)
