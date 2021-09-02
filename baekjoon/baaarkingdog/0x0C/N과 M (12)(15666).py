l, c = lambda: map(int, input().split()), 0
n, m = l()
l = sorted(l())
s, d = [0] * m,  {}


def b(c):
    if c == m:
        t = ' '.join(map(str, s))
        if t not in d:
            d[t] = 0
        return
    for i in range(n):
        if c == 0 or c > 0 and s[c-1] <= l[i]:
            s[c] = l[i]
            b(c+1)


b(c)
print('\n'.join(d))
