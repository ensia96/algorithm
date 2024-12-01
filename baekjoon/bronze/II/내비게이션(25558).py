n, a, b, c, d, *l = map(int, open(0).read().split())
T = []
for i in range(n):
    m, *l = l
    r, l = l[: 2 * m], l[2 * m :]
    (*R,) = zip([a, *r[::2], c], [b, *r[1::2], d])
    T += (sum(abs(w - y) + abs(x - z) for (w, x), (y, z) in zip(R, R[1:])),)
print(T.index(min(T)) + 1)
