import bisect
n, m = map(int, input().split())
S, M = 1, 10**9
while S < n:
    S *= 2
T = [[]for _ in ' '*2*S]
A = [*map(int, input().split())]


def U(h, i, j, k, l):
    if l > 2*S:
        return
    T[l] += h,
    t, l = (i+j)//2, l*2
    if k < t:
        U(h, i, t, k, l)
    else:
        U(h, t+1, j, k, l+1)


def F(h, i, j, k, l, x):
    if l < i or j < k:
        return 0
    if k <= i and j <= l:
        return bisect.bisect_left(T[h], h)
    m = (i+j)//2
    return F(h*2, i, m, k, l, x)+F(h*2+1, m+1, j, k, l, x)


def Q(i, j, k):
    l, r = -M, M
    while l <= r:
        m = (l+r)//2
        if F(1, 1, n, i, j, m) < k:
            l = m+1
        else:
            r = m-1


for i in range(n):
    U(A[i], 0, S, i, 1)
for i in range(2*S):
    T[i].sort()
for _ in ' '*m:
    Q(*map(int, input().split()))
