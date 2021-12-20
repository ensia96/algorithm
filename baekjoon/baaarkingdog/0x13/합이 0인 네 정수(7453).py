import sys
import bisect as T
I, R = sys.stdin.readline, range
n = int(I())
A, B, C, D = [], [], [], []
for _ in ' '*n:
    a, b, c, d = map(int, I().split())
    A, B, C, D = A+[a], B+[b], C+[c], D+[d]
a, E, F = 0, sorted(C[i]+D[j]for i in R(n)for j in R(n)), {}
for i in R(n):
    for j in R(n):
        s = A[i]+B[j]
        F[s] = F.get(s, 0)+1
print(sum(F[f]*(T.bisect_right(E, -f)-T.bisect_left(E, -f))for f in F))
