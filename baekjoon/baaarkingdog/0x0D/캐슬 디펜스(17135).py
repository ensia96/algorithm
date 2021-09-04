l, r = lambda: map(int, input().split()), range
n, m, D = l()
A, B, R = [], [[*l()]for _ in r(n)], 0


def F(i, c):
    global R
    if c == 3:
        b, k = [[B[i][j]for j in r(m)]for i in r(n)], 0
        while sum(map(sum, b)):
            e = [(f//m, f % m)for f in r(n*m)if b[f//m][f % m]]
            for X in A:
                for d, x, y in sorted((abs(n-y)+abs(X-x), x, y)for y, x in e):
                    if d <= D:
                        b[y][x], k = 0, k+b[y][x]
                        break
            b = [[0]*m]+b[:-1]
        R = max(R, k)
        return
    [A.append(p) or F(p, c+1) or A.pop() for p in r(i+1, m)]


F(-1, 0)
print(R)
