a = [[*map(int, input().split())]for _ in range(int(input()))]
b, r = [[0]*101 for _ in range(101)], [(1, 0), (0, -1), (-1, 0), (0, 1)]


def f(x, y, c, g, q):
    if c > g:
        return
    Q = [*map(lambda x: (x+1) % 4, q[::-1])]
    for p in Q:
        x, y = x+r[p][0], y+r[p][1]
        b[y][x] = 1
    f(x, y, c+1, g, q+Q)


for x, y, d, g in a:
    b[y][x] = 1
    x, y = x+r[d][0], y+r[d][1]
    b[y][x] = 1
    f(x, y, 1, g, [d])

print(sum(all(b[i+y][j+x] for y in range(2) for x in range(2))
      for i in range(100) for j in range(100) if b[i][j]))
