f = lambda: map(eval, I().split())
I = input
Y, N = 0, 1
for T in range(*f()):
    n, m, t = f()
    a = [0] * n
    v = [0] * 2
    while m:
        m -= 1
        i, x, d = f()
        a[i - 1] += (-1 < t - x < 1e3) * d
    for i in a:
        b, = f()
        v[b] += 1 / (1 + b * i / 1e4)
    print('Data Set %d: %.2f %.2f\n' % (T + 1, *v))
