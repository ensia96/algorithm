import itertools as t
l, g = lambda: map(int, input().split()), range
n, m = l()
b, d = [[*l()] for _ in g(n)], {}
p, _ = lambda x: [(i, j) for i in g(n) for j in g(n) if b[i][j] == x], 0

for u, w in p(1):
    q, v, l = [(u, w)], [0]*n**2, {}
    for y, x in q:
        for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= i < n and 0 <= j < n and not v[i*n+j]:
                v[i*n+j] = 1
                q += [(i, j)]
                if b[i][j] == 2:
                    l[(i, j)] = abs(u-i)+abs(w-j)
    d[(u, w)] = l

print(min(sum(min(d[k].get(f, 10e9) for f in c)
      for k in d) for c in t.combinations(p(2), m)))
