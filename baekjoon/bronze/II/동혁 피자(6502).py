for l in open(i := 0):
    i += 1
    a, *A = map(int, l.split())
    a or exit()
    b, c = A
    print('Pizza', i, ['fits', 'does not fit']
          [b*b+c*c > 4*a*a], 'on the table.')
