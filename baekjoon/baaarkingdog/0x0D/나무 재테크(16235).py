l, r = lambda: map(int, input().split()), range
n, m, k = l()
i, g, t = [[*l()]for _ in r(n)], [[5]*n for _ in r(n)], {}
for _ in r(m):
    x, y, z = l()
    t[(y-1, x-1)] = t.get((y-1, x-1), [])+[z]
while k:
    for y, x in t:
        at, dt = [], 0
        for a in sorted(t[(y, x)]):
            f = g[y][x] >= a
            g[y][x], at, dt = g[y][x]-a*f, at+[[], [a+1]][f], dt+[a//2, 0][f]
        t[(y, x)], g[y][x] = at, g[y][x]+dt
    t = {e: t[e] for e in t if t[e]}
    for y, x in [*t]:
        for a in t[(y, x)]:
            if not a % 5:
                for l in [(y+p-1, x+q-1) for p in r(3) for q in r(3)]:
                    if 0 <= l[0] < n and 0 <= l[1] < n:
                        t[l] = t.get(l, [])+[1]
                t[(y, x)].pop()
    for y in r(n):
        for x in r(n):
            g[y][x] += i[y][x]
    k -= 1
print(sum(map(lambda x: len(t[x]), t)))
