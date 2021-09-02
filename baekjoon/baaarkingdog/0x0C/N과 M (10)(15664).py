l, c = lambda: map(int, input().split()), 0
n, m = l()
l = sorted(l())
s, v, d = [0] * m, [0] * n, {}


def b(c, w):
    if c == m:
        t = ' '.join(map(str, s))
        if t not in d:
            d[t] = 0
        return
    for i in range(w, n):
        if not v[i]:
            s[c], v[i] = l[i], 1
            b(c+1, i)
            v[i] = 0


b(c, 0)
print('\n'.join(d))
