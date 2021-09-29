import collections as C
l, g = lambda: map(int, input().split()), range
r, c, k = l()
b = [[*l()]for _ in g(3)]
for t in g(101):
    v, h = len(b), len(b[0])
    if r <= v and c <= h and b[r-1][c-1] == k:
        exit(print(t))
    b, l = [b, [*zip(*b)]][v < h], max(v, h)
    for j in g(l):
        a, b[j] = C.Counter([*filter(None, b[j])]).most_common(), []
        a.sort(key=lambda x: x[::-1])
        for x, y in a:
            b[j] += [x, y]
    m = max(map(len, b))
    b = [(b[j]+[0]*(m-len(b[j])))[:100]for j in g(l)]
    b = [b, [*zip(*b)]][v < h]
print(-1)
