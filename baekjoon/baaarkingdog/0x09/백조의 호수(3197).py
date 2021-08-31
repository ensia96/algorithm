import sys
i, g = sys.stdin.readline, range
r, c = map(int, i().split())
m = [[*i().strip()] for _ in g(r)]
w, l, k, t = [], [], 1, 0

for i in g(r):
    for j in g(c):
        u = m[i][j]
        if u == 'L':
            l += [(i, j, k)]
            m[i][j] = [1, k]
            k += 1
        else:
            m[i][j] = [1 if u == 'X' else 0, 0]

while l:
    p = l
    l = []
    for a, b, k in p:
        for x, y in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if 0 <= x < r and 0 <= y < c:
                d, q = m[x][y]
                if d:
                    w += [(a, b)]
                    l += [(a, b, k)]
                    continue
                if q != k:
                    if q:
                        exit(print(t))
                    m[x][y][1] = k
                    p += [(x, y, k)]
    for a, b in w:
        for x, y in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if 0 <= x < r and 0 <= y < c and m[x][y][0]:
                m[x][y][0] = 0
    w = []
    t += 1
