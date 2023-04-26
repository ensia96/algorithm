for l in [*open(0)][1:]:
    x, y = l.split()
    a, b = divmod(int(y), 10)
    print('FFFFFFDCBAA'[a]+'+'*(a > 5)*(b > 6 or a > 9))
