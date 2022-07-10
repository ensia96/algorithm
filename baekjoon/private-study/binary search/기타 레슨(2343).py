n, m = map(int, input().split())
A = [*map(int, input().split())]
l, r = max(A), sum(A)
a = l
while l <= r:
    c, s, b = (l+r)//2, 0, 0
    for i in range(n):
        s += A[i]
        if s > c:
            s, b = A[i], b+1
    if b < m:
        r = c-1
    else:
        l = a = c+1
print(a)
