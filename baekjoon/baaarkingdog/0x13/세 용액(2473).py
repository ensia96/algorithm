import bisect as B
n = int(input())
A = sorted(map(int, input().split()))
a = p = 2**32
for i in range(n):
    for j in range(i+1, n):
        s = A[i]+A[j]
        l, r = B.bisect_left(A, -s), B.bisect_right(A, -s)
        for k in [l-1, l, r, r+1]:
            if not 0 <= k < n or k in [i, j]:
                continue
            t = abs(A[k]+s)
            if t < a:
                a, p = t, (A[i], A[j], A[k])
print(*sorted(p))
