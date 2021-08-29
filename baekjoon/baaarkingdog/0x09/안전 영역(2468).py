import sys

i, r = sys.stdin.readline, range
n = int(i())
m = [[*map(int, i().split())] for _ in r(n)]
v, q = [[0] * n for _ in r(n)], [(0, 0)]
d = {k: [] for k in set([b for a in m for b in a])}
v[0][0], e = 1, 0

for a, b in q:
    for k in d:
        if m[a][b] > k:
            d[k] += [(a, b)]
    for x, y in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
        if 0 <= x < n and 0 <= y < n and not v[x][y]:
            v[x][y] = 1
            q += [(x, y)]

for k in d:
    w, v = 0, [[0] * n for _ in r(n)]
    for c in d[k]:
        if not v[c[0]][c[1]]:
            w += 1
            q = [c]
            for a, b in q:
                for x, y in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
                    if 0 <= x < n and 0 <= y < n and not v[x][y] and (x, y) in d[k]:
                        v[x][y] = 1
                        q += [(x, y)]
    e = max(w, e)

print(e)
