l, r = lambda: map(int, input().split()), []
n, m = l()
l = [*sorted(l())]


def b(n, m, s=[], v=[0]*n):
    global l, r
    if len(s) == m:
        t = [*map(str, s)]
        if t not in r:
            r += [t]
            print(*t)
        return
    for i in range(n):
        if not v[i]:
            v[i] = 1
            b(n, m, s + [l[i]], v)
            v[i] = 0


b(n, m)
