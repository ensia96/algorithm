L, R = lambda: map(int, input().split()), range
a, b = L()
A = [[*L()]for _ in R(a)]
b, c = L()
B = [[*L()]for _ in R(b)]
for _ in [[sum(A[i][k]*B[k][j]for k in R(b))for j in R(c)]for i in R(a)]:
    print(*_)
