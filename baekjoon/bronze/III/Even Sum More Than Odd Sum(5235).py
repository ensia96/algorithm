for l in [*open(0)][1:]:
    x = sum(i*(1-2*(i % 2))for i in [*map(int, l.split())][1:])
    print('ETOVIDEEDN'[(x == 0)+2*(x < 0)::3])
