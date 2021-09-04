import collections as c
g = [c.deque([*input()]) for _ in range(4)]


def rotation(i, j):
    v = [0]*4
    q, v[i] = [(i, j)], 1
    for a, p in q:
        for x, y, z in [(a-1, 6, 2), (a+1, 2, 6)]:
            if 0 <= x < 4 and g[a][y] != g[x][z] and not v[x]:
                v[x] = 1
                q += [(x, -p)]
    for i, j in q:
        g[i].rotate(j)


_ = [rotation(i-1, j) for i, j in [map(int, input().split())
                                   for _ in range(int(input()))]]

print(sum([int(g[i][0])*[1, 2, 4, 8][i] for i in range(4)]))
