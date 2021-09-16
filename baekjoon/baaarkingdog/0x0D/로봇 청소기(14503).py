l, _ = lambda: map(int, input().split()), 0
n, m = l()
r, c, d = l()
b, q = [[*l()] for _ in range(n)], [(r, c, -d % 4)]

for y, x, d in q:
    b[y][x], c = 2, 0
    s = [(y, x-1), (y+1, x), (y, x+1), (y-1, x)]
    for _ in range(d, d+4):
        i, j = s[_ % 4]
        if 0 <= i < n and 0 <= j < m and not b[i][j]:
            q += [(i, j, (d+c+1) % 4)]
            break
        c += 1
    if c == 4:
        i, j = s[(d+1) % 4]
        if b[i][j] == 2:
            q += [(i, j, d)]
        else:
            break

print(sum(map(lambda x: x.count(2), b)))
