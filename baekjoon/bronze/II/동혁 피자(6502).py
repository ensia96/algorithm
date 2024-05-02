for l in open(i := 0):
    i += 1
    t = l.split()
    t[0] == '0' and exit()
    a, b, c = map(int, t)
    print('Pizza', i, ['fits', 'does not fit']
          [b*b+c*c > 4*a*a], 'on the table')
