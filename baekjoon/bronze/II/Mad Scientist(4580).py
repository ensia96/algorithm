for l in [*open(0)][:-1]:
    _, *A = map(int, l.split())
    t, *x = [0]
    for a, b in zip([0, *A], A):
        x += [t := t+1]*(b-a)
    print(*x)
