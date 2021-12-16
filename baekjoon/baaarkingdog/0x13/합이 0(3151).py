import sys
import bisect as B
I = sys.stdin.readline
n, a = int(I()), 0
A = sorted(map(int, I().split()))
for i in range(n-1):
    for j in range(1, n):
        s = A[i]+A[j]
        a += B.bisect_right(A, -s, i+1, j)-B.bisect_left(A, -s, i+1, j)
print(a)
