I = input
I()
G = [set()] * 2
for a in map(int, I().split()):
    G[a % 2].add(a)
G = max(G, key=len)
t = max(G) % 2
for i in range(1, 10**6):
    i not in G and i % 2 == t and exit(print(i))
