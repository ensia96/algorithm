for l in [*open(0)][1:]:
    D = {(l.count(i), i)for i in l}
    *A, x, y = sorted(D)
    print([y[1], '?'][x[0] == y[0] and '\n' != x[1]])
