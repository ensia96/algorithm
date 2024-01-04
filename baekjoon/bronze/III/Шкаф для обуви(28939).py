import sys
C, F = 0, lambda: map(int, sys.stdin.readline().split())
n, *_ = F()
k, p, q = F()
for _ in ' '*n:
    h, x, *A = F()
    C += sum(k*h < q*a or p*a < h for a in A)
print(C)
