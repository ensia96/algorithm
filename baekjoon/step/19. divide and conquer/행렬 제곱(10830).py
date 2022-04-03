L, R, M = lambda: map(int, input().split()), range, lambda x: x % 1000
n, B = L()
A = [[*L()]for _ in ' '*n]
C = [[i == j for j in R(n)]for i in R(n)]


def m(A, B): return [[M(sum(M(A[i][k])*M(B[k][j])
                            for k in R(n)))for j in R(n)]for i in R(n)]


t = []
while B > 0:
    t += B % 2,
    B //= 2
for i in t[::-1]:
    C = m(m(C, C), A) if i else m(C, C)
for _ in C:
    print(*_)
