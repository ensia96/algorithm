import bisect as B
n, m = map(int, input().split())
S = 1
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
        U(h, t, j, k, l+1)


def F(h, i, j, k, l, v):
    if l < i or j < k:
        return[]
    if k <= i and j <= l:
        return[h]
    m = (i+j)//2
    return v+F(h*2, i, m, k, l, v)+F(h*2+1, m+1, j, k, l, v)


def Q(i, j, k):
    v = F(1, 1, n, i, j, [])
    l, r = x, y
    while l <= r:
        m = (l+r)//2
        a = b = 0
        for i in v:
            a += B.bisect_left(T[i], m)
            b += B.bisect_right(T[i], m)
        if a < k <= b:
            print(m)
            return
        if a < k:
            l = m+1
        else:
            r = m-1


for i in range(n):
    U(A[i], 0, S, i, 1)
for i in range(2*S):
    T[i].sort()
x, y = T[1][0], T[1][-1]
for _ in ' '*m:
    Q(*map(int, input().split()))
