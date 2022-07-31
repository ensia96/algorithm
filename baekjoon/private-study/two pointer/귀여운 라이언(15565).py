n, k = map(int, input().split())
A = [*map(int, input().split())]
f = l = r = 0
c, s = A[0] < 2, n-1
while l < n:
    if c < k and r < n-1:
        r += 1
        c += A[r] < 2
    else:
        c -= A[l] < 2
        l += 1
    if c == k:
        f = 1
        s = min(s, r-l+1)
print(s if f else -1)
