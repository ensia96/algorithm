a, b, c, d, e, f, p = *map(int, open(0).read().split()), 100
a, b, c, e, f = *sorted([a, b, c]), *sorted([e, f])
x, y = (a+b+c)*d/p, (b*e+c*f)/p
print([f'two {y:.2f}', f'one {x:.2f}'][x > y])
