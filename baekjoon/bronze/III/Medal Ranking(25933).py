for l in [*open(0)][1:]:
    a, b, c, d, e, f = map(int, l.split())
    print(l+['none', 'count', 'color', 'both'][(a+b+c > d+e+f)+2*((a > d)
          or (a == d and (b > e)) or (a == d and b == e and (c > f)))]+'\n')
