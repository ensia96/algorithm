n = int(input())
A = sorted(map(int, input().split()))
l, r = 0, n-1
R, P = abs(A[l]+A[r]), (A[l], A[r])
while l-r:
    t = abs(A[l]+A[r])
    if t < R:
        R, P = t, (A[l], A[r])
    f = abs(A[l+1]+A[r]) > abs(A[l]+A[r-1])
    l, r = l+(not f), r-f
print(*P)
