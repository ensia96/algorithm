n, k = map(int, input().split())
q, m = [(n, k, 0)], [0] * 100001
m[n], l = (n, k, 0), []

for c, p, t in q:
    if m[k]:
        break
    for x in [c*2, c+1, c-1]:
        if 0 <= x < 100001 and not m[x]:
            m[x] = (x, c, m[c][2] + 1)
            q += [(x, c, m[c][2] + 1)]

c = k
while 1:
    _, c, __ = m[c]
    if c == k:
        break
    l = [c] + l

print(m[k][2])
print(*(l + [k]))
