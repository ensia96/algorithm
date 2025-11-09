i = int
I = input
while (n := i(I())) > 0:
    D = {}
    for _ in ' ' * n:
        x, y, z, N = I().split()
        D[i(x) * i(y) * i(z)] = N
    print(D[max(D)], 'took clay from', D[min(D)] + '.')
