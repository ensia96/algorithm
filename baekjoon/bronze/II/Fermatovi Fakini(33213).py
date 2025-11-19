G = [set()] * 2
for a in map(int, [*open(0)][1].split()):
    G[a % 2].add(a)
G = max(G, key=len)
for i in range([2, 1][max(G) % 2], max(G) + 3, 2):
    if i not in G:
        exit(print(i))
