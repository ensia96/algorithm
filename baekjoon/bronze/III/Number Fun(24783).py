for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    print(['Imp', 'P'][c in [a+b, a-b, a*b, a/b, b+a, b-a, b*a, b/a]]+'ossible')
