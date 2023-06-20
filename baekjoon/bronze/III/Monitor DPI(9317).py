for l in [*open(0)][:-1]:
    a, b, c = map(float, l.split())
    x = (16*a)/337**.5
    y = (9/16)*x
    print(f'Horizontal DPI: {b/x:.2f}')
    print(f'Vertical DPI: {c/y:.2f}')
