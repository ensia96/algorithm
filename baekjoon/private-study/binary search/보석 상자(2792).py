n, m = map(int, input().split())
A = [int(input())for _ in ' '*m]
l, r = 1, max(A)
while l <= r:
    m = (l+r)//2
    if sum(a//m+bool(a % m)for a in A) > n:
        l = m+1
    else:
        r = m-1
print(l)
