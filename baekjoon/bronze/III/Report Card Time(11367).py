for l in [*open(0)][1:]:
    x, y = l.split()
    a, b = divmod(int(y), 10)
    print('FFFFFFDCBA'[a]+'+'*(a > 5)*(b > 6))
