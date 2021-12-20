import sys
import collections as Y
I, R = sys.stdin.readline, range
n = int(I())
A, B, C, D = [], [], [], []
for _ in R(n):
    a, b, c, d = map(int, I().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
a, E = 0, Y.defaultdict(int)
for i in R(n):
    for j in R(n):
        E[A[i]+B[j]] += 1
for i in R(n):
    for j in R(n):
        a += E.get(-C[i]-D[j], 0)
print(a)
