for l in [*open(0)][1:]:
    x, y = divmod(int(l), 100)
    print('YNEOS'[(x*x+y*y) % 7 != 1::2])
