i = input
l, c = map(int, i().split())
s, v = sorted(i().split()), [0] * c


def u(n, p, d, f, h):
    if f and h > 1 and d == l:
        print(n)
        return
    for i in range(p, c):
        if not v[i]:
            v[i] = 1
            if s[i] in 'aeiou':
                u(n+s[i], i, d+1, f+1, h)
            else:
                u(n+s[i], i, d+1, f, h+1)
            v[i] = 0


u('', 0, 0, 0, 0)
