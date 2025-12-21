I = input
P = print
for t in range(int(I())):
    m, n = map(int, I().split())
    M = [int(I())for _ in ' ' * m]
    A = 0
    for _ in ' ' * n:
        h, w, d, i = map(int, I().split())
        A += h * w * d * M[i - 1]
    P(f'Data Set {t + 1}:')
    P(A)
