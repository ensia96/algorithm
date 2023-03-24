for l in open(0):
    a, b, c = sorted(map(int, l.split()))
    a*b*c and print(['Scalene', 'Isosceles', 'Invalid', 'Equilateral']
                    [2*(a+b <= c) or (a == b)+(b == c)+(c == a)])
