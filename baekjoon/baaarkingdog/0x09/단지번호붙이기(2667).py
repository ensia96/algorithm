i, r = input, range

n = int(i())
m = [[*map(int, i())] for _ in r(n)]
a, l = 0, []

for i in r(n):
    for j in r(n):
        if m[i][j]:
            a += 1
            m[i][j] = 0
            c, q = 1, [(i, j)]
            for u, v in q:
                for x, y in [(u+1, v), (u-1, v), (u, v+1), (u, v-1)]:
                    if 0 <= x < n and 0 <= y < n and m[x][y]:
                        m[x][y] = 0
                        c += 1
                        q += [(x, y)]
            l.append(c)

for x in [a] + sorted(l):
    print(x)
