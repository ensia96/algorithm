l, g = [*map(int, input().split())], range
a, b, p = 0, [[*g(0, 42, 2)]]+[[0]*21 for _ in g(3)], [(0, 0)]*4
for y, x, n in [(1, 5, 13), (2, 5, 16), (3, 5, 19), (1, 10, 22), (2, 10, 24),
                (1, 15, 28), (2, 15, 27), (3, 15, 26), (1, 20, 35), (2, 20, 30), (3, 20, 25)]:
    b[y][x] = n


def s(i, c):
    global a
    if i == 10:
        a = max(a, c)
        return
    for o in g(4):
        if p[o] == (2, o):
            continue
        y, x = p[o]
        h, w, r = [(y, x, l[i]), (y+1, x, l[i]-1)][x in (5, 10, 15)]
        h, w = [(h, w), (3, 20)][(h, w) in [(4, 5), (3, 10), (4, 15)]]
        for m in g(r):
            h, w = [[(h+1, w), (h, w+1)][not h], (h-1, w)][w == 20]
            h, w = [(h, w), (3, 20)][(h, w) in [(4, 5), (3, 10), (4, 15)]]
            if h < 0:
                h, w = 2, o
                break
        if (h, w) in p:
            return
        p[o] = (h, w)
        s(i+1, c+b[h][w])
        p[o] = (y, x)


s(0, 0)
print(a)
