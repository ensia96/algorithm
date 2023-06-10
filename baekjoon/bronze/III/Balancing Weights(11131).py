for l in [*open(0)][2::2]:
    x = sum(map(int, l.split()))
    print(['Equilibrium', 'Left', 'Right'][(x < 0)+2*(x > 0)])
