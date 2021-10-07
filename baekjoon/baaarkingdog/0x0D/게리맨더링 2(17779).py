u, g = input, range
n = int(u())
h, _ = lambda a, b: (0 <= a < n)*(0 <= b < n), 0
m = [[*map(int, u().split())]for _ in g(n)]


def check(x, y, p, q):
    a, b = [0]*5, [[0]*n for _ in g(n)]
    for i, j in [(x+i, y-i)for i in g(p+1)]:
        for r, c in [(i+k, j+k)for k in g(q+1)]:
            if not h(r, c):
                return 10**9
            b[r][c], a[4] = 1, a[4]+m[r][c]
    for o in g(n*n):
        i, j = o//n, o % n
        if b[i][j]:
            continue
        if all(h(r, c) and (b[r][c] == 1)for r, c in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]):
            b[i][j], a[4] = 1, a[4]+m[i][j]
        else:
            a[0] += (i < x+p)*(j <= y)*m[i][j]
            a[1] += (i <= x+q)*(y < j)*m[i][j]
            a[2] += (x+p <= i)*(j < y+q-p)*m[i][j]
            a[3] += (x+q < i)*(y+q-p <= j)*m[i][j]
    return max(a)-min(a)


print(min(check(i, j, k, l)for i in g(n) for j in g(n)
      for k in g(1, j+1) for l in g(1, n-j+1)))
