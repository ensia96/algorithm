a, r = range, ((1, 0), (0, -1), (-1, 0), (0, 1))
b = [[0]*101 for _ in a(101)]
for _ in a(int(input())):
    x, y, d, g = map(int, input().split())
    b[y][x], q = 1, [d]
    for _ in a(g):
        q += [(i+1) % 4 for i in q[::-1]]
    for p in q:
        x, y = x+r[p][0], y+r[p][1]
        b[y][x] = 1
print(sum(all(b[i+y][j+x] for y in a(2) for x in a(2))
      for i in a(100) for j in a(100)))
