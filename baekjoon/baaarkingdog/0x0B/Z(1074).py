def z(n, r, c, x=0, y=0, v=0):
    if (r, c) == (x, y):
        return v
    if n == 0:
        return 0
    q = 2**(n-1)
    t = q**2
    for p, a, b in [(0, x, y), (t, x, y+q), (2*t, x+q, y), (3*t, x+q, y+q)]:
        if a <= r <= a + q and b <= c <= b + q:
            l = z(n-1, r, c, a, b, v + p)
            if l:
                return l


print(z(*map(int, input().split())))
