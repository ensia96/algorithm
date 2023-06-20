for l in [*open(0)][:-1]:
    i = eval(l.replace(*' -'))
    print((i-3*(i % 2))//2*(i > 1), (i % 2)*(i > 1))
