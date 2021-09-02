l, a = lambda: map(int, input().split()), 0
n, s = l()
l, v = [*l()], [0]*n


def b(c, d, x):
    global a
    if d == n:
        return
    for i in range(x, n):
        if not v[i]:
            t, v[i] = c + l[i], 1
            b(t, d+1, i)
            a += t == s
            v[i] = 0


b(0, 0, 0)
print(a)
