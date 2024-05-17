import bisect
n, q, *A = map(int, open(0).read().split())
T = [sum(A[:i])for i in range(n)]
for a in A[n:]:
    print(bisect.bisect_right(T, a))
