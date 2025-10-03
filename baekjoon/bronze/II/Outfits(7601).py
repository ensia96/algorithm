I, P, R, t = input, print, range, 1
while '00' < (l := I()):
    n, d = map(int, l.split())
    a, b = int(I()), int(I())
    a, b = [i for i in R(1, n + 1)if i != a], [i for i in R(n, 0, -1)if i != b]
    P("Scenario", t)
    for i in R(d):
        x, y = map(int, I().split())
        P("Day", i + 1, ['OK', 'ALERT'][a[x - 1] == b[y - 1]])
    t += 1
