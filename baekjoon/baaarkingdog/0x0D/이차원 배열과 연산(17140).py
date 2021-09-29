import collections as C
l, g = lambda: map(int, input().split()), range
r, c, k = l()
b = [[*l()]for _ in g(3)]
for t in g(101):
    v, h = len(b), len(b[0])
    if r <= v and c <= h and b[r-1][c-1] == k:
        exit(print(t))
    f = v < h
    b = [b, [*zip(*b)]][f]
    m, l = 0, len(b)
    for j in g(l):
        a, b[j] = C.Counter([*filter(None, b[j])]).most_common(), []
        a.sort(key=lambda x: x[::-1])
        for x, y in a:
            b[j] += [x, y]
        nl = len(a)
        m = [m, nl*2][m < nl*2]
    for j in g(l):
        for _ in g(m-len(b[j])):
            b[j] += [0]
        b[j] = b[j][:100]
    b = [b, [*zip(*b)]][f]
print(-1)
