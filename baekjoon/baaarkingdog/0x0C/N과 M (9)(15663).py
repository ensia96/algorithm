l, r = lambda: map(int, input().split()), []
n, m = l()
l = [*sorted(l())]


def b(n, m, s=[], v=[]):
    global l, r
    if len(s) == m and s not in r:
        r += [s]
        print(*map(str, s))
        return
    for i in range(n):
        if i not in v:
            b(n, m, s + [l[i]], v+[i])


b(n, m)
