for l in open(0):
    a, b, c = map(int, l.split())
    print('SN'[(a*a+144)**.5/c > 12/b])
