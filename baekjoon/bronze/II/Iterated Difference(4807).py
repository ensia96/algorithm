for l in [*open(i := 0)][1::2]:
    *l, = map(int, l.split())
    c = 0
    while c < 1e3 > 1 < len({*l}):
        l = [abs(i-j)for i, j in zip(l, (2*l)[1:])]
        c += 1
    i += 1
    print(f'Case {i}:', ['not attained', f"{c} iterations"][c < 1000])
