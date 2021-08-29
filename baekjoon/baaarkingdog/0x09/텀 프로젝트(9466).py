i, t, r = input, int, range

for _ in r(t(i())):
    n = t(i())
    s = [int(a) - 1 for a in i().split()]
    m = [[0] * n for _ in r(n)]
    for a in r(n):
        m[a][s[a]] = 1
        m[a][s[s[a]]] = 1
    for z in m:
        print(z)
    for a in r(n):
        for b in r(n):
            if m[a][b] != m[b][a]:
                m[a][b] = m[b][a] = 0
    print(sum(not any(l) for l in m))
