I = input
P = print
f = lambda: map(int, I().split())
for t in range(*f()):
    m, n = f()
    M = [int(I())for _ in ' ' * m]
    A = 0
    for _ in ' ' * n:
        h, w, d, i = f()
        A += h * w * d * M[i - 1]
    P(f'Data Set {t + 1}:')
    P(A)
