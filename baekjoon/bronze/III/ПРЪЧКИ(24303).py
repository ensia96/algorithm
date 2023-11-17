a, b, c, d, e, f, x = map(int, input().split())
D = {a: d, b: e, c: f}
a = 0
for i in sorted(D)[::-1]:
    i*D[i] > x and exit(print(-(x//-i)+a))
    a += D[i]
    x -= i*D[i]
print(0)
