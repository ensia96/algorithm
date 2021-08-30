import sys

i, r = sys.stdin.readline, range
n, p, q, f = int(i()), 0, [], 0
b, s = [[*map(int, i().split())] for _ in r(n)], [[0] * n for _ in r(n)]

for c in r(n):
    for d in r(n):
        if b[c][d] and not s[c][d]:
            p += 1
            t, s[c][d] = [(c, d)], p
            for u, v in t:
                for x, y in [(u+1, v), (u-1, v), (u, v+1), (u, v-1)]:
                    if 0 <= x < n and 0 <= y < n and not s[x][y]:
                        s[x][y] = p
                        if b[x][y]:
                            t += [(x, y)]
                        else:
                            b[x][y] = 1
                            q += [(x, y, p)]

for c, d, p in q:
    if f:
        break
    s[c][d] = p
    for x, y in [(c+1, d), (c-1, d), (c, d+1), (c, d-1)]:
        if 0 <= x < n and 0 <= y < n and s[c][d] != s[x][y]:
            if b[x][y]:
                f = b[c][d] + b[x][y]
            else:
                b[x][y], s[x][y] = b[c][d] + 1, p
print(f)
