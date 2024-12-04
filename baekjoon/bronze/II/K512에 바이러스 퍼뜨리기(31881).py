import sys

f = lambda: [*map(int, sys.stdin.readline().split())]
n, q = f()
C = [0] * -~n
s = n
for _ in " " * q:
    a, *A = f()
    if len(A):
        s += C[A[0]] - (a < 2)
        C[A[0]] = a < 2
    else:
        print(s)
