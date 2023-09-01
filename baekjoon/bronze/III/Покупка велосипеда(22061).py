for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    print('YNEOS'[max(0, c//2-b)*2+c % 2 > a::2])
