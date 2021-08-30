import sys
i, g = sys.stdin.readline, range

while 1:
    l, r, c = map(int, i().split())
    if not l:
        break
    a, m = 0, [[[*i().strip()] for __ in g(r + 1)][:-1] for _ in g(l)]

    for d in g(l):
        for e in g(r):
            for f in g(c):
                if m[d][e][f] == 'S':
                    m[d][e][f] = 0
                    q = [(d, e, f)]
                if m[d][e][f] == 'E':
                    m[d][e][f] = '.'
                    n = (d, e, f)

    for d, e, f in q:
        if (d, e, f) == n:
            a = m[d][e][f]
            break
        for z, y, x in [(d+1, e, f), (d-1, e, f), (d, e+1, f), (d, e-1, f), (d, e, f+1), (d, e, f-1)]:
            if 0 <= z < l and 0 <= y < r and 0 <= x < c and m[z][y][x] == '.':
                m[z][y][x] = m[d][e][f] + 1
                q += [(z, y, x)]

    print(f'Escaped in {a} minute(s).' if a else 'Trapped!')
