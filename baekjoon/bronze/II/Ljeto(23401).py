G = [[]for _ in range(8)]
for l in [*open(0)][1:]:
    t, a, b = map(int, l.split())
    G[a - 1] += t,
G = [100 * len(g) + 50 * sum(j - i <= 10 for i, j in zip(g, g[1:]))for g in G]
print(sum(G[:4]), sum(G[4:]))
