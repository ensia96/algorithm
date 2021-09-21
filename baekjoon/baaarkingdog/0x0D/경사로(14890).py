_, g = lambda: map(int, input().split()), range
n, l = _()
a, b = 0, [[*_()]for __ in g(n)]

for _ in g(2):
    for i in g(n):
        h, c, v = b[i][0], 1, [1]+[0]*(n-1)
        for j in g(1, n):
            v[j] = 1
            if h == b[i][j]:
                c += 1
            elif b[i][j] == h+1 and c >= l:
                h, c = b[i][j], 1
            elif b[i][j] == h-1 and c >= 0:
                h, c = h-1, -(l-1)
            else:
                v[j] = 0
                break
        a += all(v) and c >= 0
    b = [[b[n-1-j][i] for j in g(n)] for i in g(n)]

print(a)
