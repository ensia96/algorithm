l, r = lambda: map(int, input().split()), range
n, m, t = l()
b, c = [[*l()]for _ in r(n)], n*m
for _ in r(t):
    x, d, k, f = *l(), 1
    k = [-k, k][d]
    b = [b[i]if(i+1) % x else b[i][k:]+b[i][:k]for i in r(n)]
    for q, v in (([(i, j)], b[i][j])for i in r(n)for j in r(m)if b[i][j]):
        for y, x in q:
            for h, w in [(y+1, x % m), (y-1, x % m), (y, (x+1) % m), (y, (x-1) % m)]:
                if (0 <= h < n) and b[h][w] == v:
                    b[h][w], f, c = 0, 0, c-1
                    q += [(h, w)]
    if f*c:
        a = sum(map(sum, b))/c
        b = [[*map(lambda u:u+(-(a < u)+(a > u))*bool(u), e)]for e in b]
print(sum(map(sum, b)))
