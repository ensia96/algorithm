I = input
n = m = x = y = 0
for _ in ' ' * int(I()):
    t, a, b = map(int, I().split())
    z = 100 + 50 * (x == a and y + 10 >= t)
    n, m, x, y = n + z * (a < 5), m + z * (a > 4), a, t
print(n, m)
