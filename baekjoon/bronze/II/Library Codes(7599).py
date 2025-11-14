I = input
P = print
while (L := I()) > '#_':
    N, f = L.split()
    f = int(f)
    P(N, 'Library')
    for i in range(int(I())):
        w, T = I().split()
        P('Book', i + 1, ['horizontal', 'vertical'][int(w) < len(T) * f + 2])
