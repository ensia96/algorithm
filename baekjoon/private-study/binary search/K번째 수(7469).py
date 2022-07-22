import bisect
n, m = map(int, input().split())
S, M = 1, 10**9
while S < n:
    S *= 2
T = [[]for _ in ' '*2*S]
A = [*map(int, input().split())]


def U(i, l, r):
    if l == r:
        T[i] = [A[l-1]]
    else:
        m = (l+r)//2
        U(i*2, l, m)
        U(i*2+1, m+1, r)
        T[i] = sorted(T[i*2]+T[i*2+1])


def F(h, i, j, k, l, x):
    if l < i or j < k:
        return 0
    if k <= i and j <= l:
        return bisect.bisect_left(T[h], x)
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
    print(r)


U(1, 1, n)
for _ in ' '*m:
    Q(*map(int, input().split()))
