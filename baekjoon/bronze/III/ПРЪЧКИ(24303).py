a, b, c, d, e, f, x = map(int, input().split())
D = {a: d, b: e, c: f}
a = b = 0
for i in sorted(D)[::-1]:
    for j in range(D[i]):
        a += i
        b += 1
        a >= x and exit(print(b))
print(0)
