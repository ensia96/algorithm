n, m = map(int, input().split())
A = [int(input())for _ in ' '*n]
l, r = 0, sum(A)
while l <= r:
    k = t = (l+r)//2
    c = 0
    for a in A:
        if a > t:
            t = k
            c += 1
        t -= a
        if t < 0:
            c += m
            break
    if c >= m:
        l = k+1
    else:
        r = k-1
print(l)
