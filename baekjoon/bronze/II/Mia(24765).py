f = lambda x, y: (((x * y == 2) * 10 + (x == y) * x)
                  * 10 + max(x, y)) * 10 + min(x, y)
while '1' < (l := input()):
    a, b, c, d = map(int, l.split())
    x, y = f(a, b), f(c, d)
    print([f'Player {1 + (y > x)} wins.', 'Tie.'][x == y])
