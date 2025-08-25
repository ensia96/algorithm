I = input
while (C := I()) != '#':
    M, S = map(int, I().split())
    for _ in ' '*int(I()):
        t, a = I().split()
        a = int(a)
        S = [min(M, S+a), max(0, S-a)][t == 'S']
    print(C, S)
