import sys

i, r = sys.stdin.readline, range
n, e = int(i()), 0
m = [[*map(int, i().split())] for _ in r(n)]
s, q = set([b for a in m for b in a]), [(0, 0)]

for h in s:
    w, v = 0, [[0] * n for _ in r(n)]
    for i in r(n):
        for j in r(n):
            if m[i][j] > h and not v[i][j]:
                w += 1
                q = [(i, j)]
                for a, b in q:
                    for x, y in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
                        if 0 <= x < n and 0 <= y < n and not v[x][y] and m[x][y] > h:
                            v[x][y] = 1
                            q += [(x, y)]
    e = max(w, e)

print(e)
