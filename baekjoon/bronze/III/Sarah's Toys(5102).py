for l in [*open(0)][:-1]:
    i = eval(l.replace(*' -'))
    x, y = divmod(i, 2)
    print(x*(i > 3), y*(i > 2))
