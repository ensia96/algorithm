import bisect as B
n, s = map(int, input().split())
A = [*map(int, input().split())]
L, R = [0], [0]
for a in A[:n//2]:
    L += [l+a for l in L]
for a in A[n//2:]:
    R += [r+a for r in R]
C = sum(l == s for l in L[1:])
L.sort()
print(C+sum(B.bisect_right(L, s-r)-B.bisect_left(L, s-r)for r in R[1:]))
