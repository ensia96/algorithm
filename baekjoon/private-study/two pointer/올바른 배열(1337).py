n = int(input())
A = sorted(int(input())for _ in ' '*n)
l = r = 0
c = 5
while l <= r < n:
    if A[r] < A[l]+5:
        c = min(c, 5-r+l-1)
        r += 1
    else:
        l += 1
print(c)
