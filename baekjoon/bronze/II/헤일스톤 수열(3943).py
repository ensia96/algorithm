for l in [*open(0)][1:]:
    i = I = int(l)
    while i != 1:
        if i % 2:
            i = i*3+1
        else:
            i //= 2
        I = max(I, i)
    print(I)
