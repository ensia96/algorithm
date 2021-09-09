m, c, f = [[*input().strip()] for _ in range(12)], 0, 1


def ppuyo(i, j, c):
    v = [[0]*6 for _ in range(12)]
    v[i][j], q = 1, [(i, j)]
    for i, j in q:
        for y, x in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= y < 12 and 0 <= x < 6 and not v[y][x] and m[y][x] == c:
                q += [(y, x)]
                v[y][x] = 1
    pang = len(q) > 3
    if pang:
        for y, x in q:
            m[y][x] = '.'
    return pang


def swipe():
    for i in range(12)[::-1]:
        for j in range(6):
            if m[i][j] != '.':
                q = [i]
                for h in q:
                    if h+1 < 12 and m[h+1][j] == '.':
                        m[h][j], m[h+1][j] = m[h+1][j], m[h][j]
                        q += [h+1]


while f:
    f = 0
    for i in range(12)[::-1]:
        for j in range(6):
            if m[i][j] != '.' and ppuyo(i, j, m[i][j]):
                swipe()
                print()
                for _ in m:
                    print(_)
                c += 1
                f = 1

print(c)
