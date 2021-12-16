import sys
import bisect as B
I = sys.stdin.readline
l, r = B.bisect_left, B.bisect_right
n, a = int(I()), 0
A = sorted(map(int, I().split()))
for i in range(n-1):
    for j in range(1, n):
        s = A[i]+A[j]
        a += r(A, -s, i+1, j) != l(A, -s, i+1, j)
print(a)
