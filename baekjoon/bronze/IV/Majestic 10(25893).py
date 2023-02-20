x = 'double'
for _ in ' '*int(input()):
    a, b, c = map(int, input().split())
    print(a, b, c)
    y = (a > 9)+(b > 9)+(c > 9)
    print(['zlich', x, x+'-'+x, 'triple-'+x][y])
    print()
