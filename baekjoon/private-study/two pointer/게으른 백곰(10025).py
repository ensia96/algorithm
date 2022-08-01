n, k = map(int, input().split())
A = sorted((*map(int, input().split()[::-1]),)for _ in ' '*n)
x = l = r = 0
c = A[0][1]
while l <= r < n:
    if A[l][0]+2*k < A[r][0]:
        x -= A[l][1]
        l += 1
    else:
        x += A[r][1]
        r += 1
        c = max(c, x)
print(c)
