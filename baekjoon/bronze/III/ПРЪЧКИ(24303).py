a, b, c, d, e, f, x = map(int, input().split())
D = {a: d, b: e, c: f}
a = 0
for i in sorted(D)[::-1]:
    y = min(x//i, D[i])
    x -= i*y
    a += y
print(a*(x < 1))
