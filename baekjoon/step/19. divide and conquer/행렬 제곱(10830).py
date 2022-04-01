L, R = lambda: map(int, input().split()), range
n, B = L()
A = [[*L()]for _ in ' '*n]
C = [[i == j for j in R(n)]for i in R(n)]


def m(A, B): return [[sum(A[i][k]*B[k][j]
                          for k in R(n)) % 1000 for j in R(n)]for i in R(n)]


while B:
    if B % 2:
        C = m(A, C)
    A, B = m(A, A), B//2
for _ in C:
    print(*_)
