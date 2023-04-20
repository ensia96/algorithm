for l in [*open(0)][1:]:
    a, b = l.split()
    x, y = {'kg': (2.2046, 'lb'), 'lb': (0.4536, 'kg'),
            'l': (0.2642, 'g'), 'g': (3.7854, 'l')}[b]
    print(f'{float(a)*x:.4f}', b)
