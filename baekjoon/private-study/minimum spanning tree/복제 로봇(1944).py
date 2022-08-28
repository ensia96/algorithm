import heapq as H
n, m = map(int, input().split())
A = [input()for _ in ' '*n]
V, E, G = {}, [], [*range(m+1)]
c = 0
for i in range(n):
    for j in range(n):
        if A[i][j] == 'S':
            V[(i, j)] = 0
        if A[i][j] == 'K':
            c += 1
            V[(i, j)] = c

for x, y in V:
    Q, v, c = [(x, y)], [n*[0]for _ in ' '*n], 0
    v[x][y] = 1
    while Q:
        c += 1
        q = []
        for i, j in Q:
            for a, b in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 < a < n and 0 < b < n and A[a][b] != '1' and not v[a][b]:
                    v[a][b] = 1
                    if A[a][b] in 'SK':
                        E += (c, V[(x, y)], V[(a, b)]),
                    q += [(a, b)]
        Q = q


def f(x):
    if G[x]-x:
        G[x] = f(G[x])
    return G[x]


A = c = 0
for x, y, z in sorted(E):
    y, z = f(y), f(z)
    if y != z:
        G[max(y, z)] = min(y, z)
        A += x
        c += 1
print(-1 if c-m else A)
