for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    print('TNAIKE'[b % a > 0::2])
