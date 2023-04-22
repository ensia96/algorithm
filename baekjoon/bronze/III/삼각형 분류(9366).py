for i, l in enumerate([*open(0)][1:]):
    a, b, c = sorted(map(int, l.split()))
    x, y, z = a == b, b == c, c == a
    print(f'Case #{i+1}:', ('invalid!', (('scalene', 'isosceles')
          [bool(x+y+z)], 'equilateral')[x*y*z])[a+b > c])
