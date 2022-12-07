n = int(input())
*A, = map(int, input().split())
R = 3*A[0]
C = [0]*n
for i in range(1, n):
    t = min(A[i], A[i-1])
    A[i] -= t
    C[i] += t
    R += 2*t
    t = min(A[i], C[i-1])
    A[i] -= t
    R += 2*t+3*A[i]
print(R)
