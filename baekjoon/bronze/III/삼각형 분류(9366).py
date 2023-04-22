for i, l in enumerate(open(0)):
    a, b, c = sorted(map(int, l.split()))
    x, y, z = a == b, b == c, c == a
    i and print(f'Case #{i}:', ('invalid!', (('scalene', 'isosceles')[
                x+y+z], 'equilateral')[x*y*z])[a+b > c])
