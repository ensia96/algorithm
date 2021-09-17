n, m = map(int, input().split())
a = [[*input()] for _ in range(n)]
_, u = lambda i, j, d: [(i+1, j), (i-1, j), (i, j+1), (i, j-1)][d], 11


for i in range(n):
    for j in range(m):
        if a[i][j] == 'R':
            r = (i, j, 0)
        if a[i][j] == 'B':
            b = (i, j, 1)


def check(i, j):
    v = []
    for d in range(4):
        y, x = _(i, j, d)
        if a[y][x] != '#':
            v += [d]
    return v


def move(y, x, l, d):
    q = [(y, x)]
    for i, j in q:
        v, h = _(i, j, d)
        if a[v][h] == '.':
            q += [(v, h)]
        elif a[v][h] == 'O':
            a[y][x] = '.'
            return v, h
        elif a[v][h] == '#':
            a[y][x] = '.'
            a[i][j] = 'RB'[l]
            return i, j
        else:
            return i, j


def t(r, b, c):
    global a, u
    if u <= c:
        return
    for d in range(4):
        i, j = move(*r, d)
        h, k = move(*b, d)
        if (i, j) == (r[0], r[1]):
            i, j = move(*r, d)
        if a[h][k] == 'O':
            a[b[0]][b[1]] = 'B'
            return
        if a[i][j] == 'O':
            a[r[0]][r[1]] = 'R'
            u = c
            return
        t((i, j, 0), (h, k, 1), c+1)
        a[i][j] = a[h][k] = '.'
        a[r[0]][r[1]], a[b[0]][b[1]] = 'R', 'B'


t(r, b, 1)
print(u if u != 11 else -1)
