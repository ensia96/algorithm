i, I = int, input
for _ in ' '*i(I()):
    D = {}
    for _ in ' '*i(I()):
        a, b = I().split()
        a = i(a)
        D[a] = b
    print(D[max(D)])
