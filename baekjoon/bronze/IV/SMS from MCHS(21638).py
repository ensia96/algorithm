a, b = map(int, input().split())
c, d = map(int, input().split())
x, y, z = c < 0 and d > 9, c < a, b < d
x+y + \
    z and print(
        'A storm warning for tomorrow! Be careful and stay home if possible!'if x else f'MCHS warns! {"Low temperature"if y else"Strong wind"} is expected tomorrow.')
