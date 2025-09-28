R = range
l, *L = open(0)
x, y, _ = map(int, l.split())
D = [x * [0]for _ in ' ' * y]
for l in L:
    a, b, c, d = map(int, l.split())
    for i in R(b - 1, d):
        for j in R(a - 1, c):
            D[i][j] = 1
print(sum(map(sum, D)))
