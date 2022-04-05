n = int(input())
k = int(input())
l, r = 1, k
while l <= r:
    m = (l+r)//2
    if sum(min(m//i, n)for i in range(1, n+1)) >= k:
        r, A = m-1, m
    else:
        l = m+1
print(A)
