c, r = lambda y, x, i, j: (0 <= y+i < 10)*(0 <= x+j < 10), range
A, b, t = 10**9, [[*map(int, input().split())]for _ in r(10)], [0]*6


def B(p, s):
    global A
    if sum(t) >= A:
        return
    if (p == 100)+(not s):
        A = min(A, sum(t))
        return
    y, x = p//10, p % 10
    if not b[y][x]:
        return B(p+1, s)
    for l in r(5, 0, -1):
        if not t[l] < 5:
            continue
        a = [(y+i, x+j)for i in r(l)
             for j in r(l)if c(y, x, i, j) and b[y+i][x+j]]
        if len(a) != l*l:
            continue
        t[l] += 1
        for y, x in a:
            b[y][x] = 0
        B(p+l, s-l*l)
        for y, x in a:
            b[y][x] = 1
        t[l] -= 1


B(0, sum(map(sum, b)))
print([A, -1][A == 10**9])
