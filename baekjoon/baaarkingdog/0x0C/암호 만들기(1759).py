i = input
l, c = map(int, i().split())
s, v = sorted(i().split()), [0] * c


def u(n, p, d, f, h):
    if f and h > 1 and d == l:
        print(n)
        return
    for i in range(p, c):
        if not v[i]:
            if s[i] in 'aeiou':
                f += 1
            else:
                h += 1
            v[i] = 1
            u(n+s[i], i, d+1, f, h)
            v[i] = 0


u('', 0, 0, 0, 0)
