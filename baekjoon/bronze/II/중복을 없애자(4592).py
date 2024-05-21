for l in [*open(0)][:-1]:
    _, a, *A = map(int, l.split())
    l = [a]
    for a in A:
        if l[-1] != a:
            l += a,
    print(*l, '$')
