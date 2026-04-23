a, b, s = map(int, input().split())
D = (a - b)**2 + 4 * s
r = round(D**.5)
print([-1, a + b + r >> 1][r * r == D])
