print('Gnomes:')
for _ in ' '*int(input()):
    a, b, c = map(int, input().split())
    print(['Uno', 'O'][a > b > c or a < b < c]+'rdered')
