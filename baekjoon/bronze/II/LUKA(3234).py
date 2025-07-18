a, b, c = open(0)
x, y = map(int, a.split())
n = m = 0
L = []
for i in range(-1, int(b)):
    k, l = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]['ISZJ'.find(c[i])]
    n += k
    m += l
    if 2 > abs(x-n) and abs(y-m) < 2:
        L += i+1,
print(*(L or [-1]))
