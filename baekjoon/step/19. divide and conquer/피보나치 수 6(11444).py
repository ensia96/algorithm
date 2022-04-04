R = range(2)
n = int(input())
p = 1000000007
A = [[*R], [1]*2]
C = A[:]


def m(A, B): return [[sum(A[i][k]*B[k][j]for k in R) % p for j in R]for i in R]


while n:
    if n % 2:
        C = m(A, C)
    A, n = m(A, A), n//2
print(C[0][0])
