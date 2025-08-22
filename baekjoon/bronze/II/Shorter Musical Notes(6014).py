from bisect import bisect_right
n, q, *L = map(int, open(0).read().split())
A = [0]
for a in L[:n]:
    A += a+A[-1],
for l in L[n:]:
    print(bisect_right(A, l))
