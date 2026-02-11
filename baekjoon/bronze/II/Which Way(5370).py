for l in open(0):
    x, y = map(f'{int(l):b}'.count, '01')
    print(x - y and 'rliegfhtt'[x > y::2] or 'straight')
