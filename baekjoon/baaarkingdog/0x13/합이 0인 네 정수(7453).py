import sys
import bisect as X
import collections as Y
I, R = sys.stdin.readline, range
n = int(I())
A, B, C, D = [], [], [], []
for _ in ' '*n:
    a, b, c, d = map(int, I().split())
    A, B, C, D = A+[a], B+[b], C+[c], D+[d]
a, E, F = 0, sorted(C[i]+D[j]for i in R(n)for j in R(n)), Y.defaultdict(int)
for i in R(n):
    for j in R(n):
        F[A[i]+B[j]] += 1
print(sum(F[f]*(X.bisect_right(E, -f)-X.bisect_left(E, -f))for f in F))
