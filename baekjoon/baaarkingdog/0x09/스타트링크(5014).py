import collections as c
f, s, g, u, d = map(int, input().split())
a, b, q = 'use the stairs', [0] * (f + 1), c.deque([(s, 0)])

while q:
    p, c = q.popleft()
    if p == g:
        a = c
        break
    if b[p]:
        continue
    b[p] = 1
    for m in [p + u, p - d]:
        if 0 < m <= f and not b[m]:
            q += [(m, c + 1)]

print(a)
