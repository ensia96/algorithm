a, b, c, i, j, k, x, y, z = open(0).read().split()
print(''.join(map(str, sorted(map(int, [b[2:], j[2:], y[2:]])))))
D = {a: c, i: k, x: z}
print(''.join(i for _, i in sorted(
    (int(n), m[:1])for n, m in D.items())[::-1]))
