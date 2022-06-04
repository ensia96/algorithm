n = range(5)
m, f = min, lambda: [5*[8**8]for i in n]
D = f()
D[0][0] = 0
for p in map(int, input().split()[:-1]):
    d = f()
    for i in n:
        for j in n:
            t = i and [1, 3, 4, 3][(p-i) % 4] or 2
            d[p][j] = m(d[p][j], D[i][j]+t)
            d[j][p] = m(d[j][p], D[j][i]+t)
    D = d
print(m(map(m, D)))
