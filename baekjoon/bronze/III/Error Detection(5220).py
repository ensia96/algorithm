for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    print(['Corrupt', 'Valid'][bin(a).count('1') % 2 == b])
