import sys
import bisect as X
import collections as Y
I, R = sys.stdin.readline, range
n = int(I())
A, B, C, D = [], [], [], []
for _ in ' '*n:
    a, b, c, d = map(int, I().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
a, E, F = 0, [], Y.defaultdict(int)
for i in R(n):
    for j in R(n):
        F[A[i]+B[j]] += 1
        E.append(C[i]+D[j])
E.sort()
print(sum(F[f]*(X.bisect_right(E, -f)-X.bisect_left(E, -f))for f in F))
