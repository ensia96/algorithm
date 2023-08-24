for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    print(f'{a*b/(a+b):.1f}')
