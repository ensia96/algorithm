for _ in ' '*int(input()):
    a, b, c, d = map(int, input().split())
    print('Eurecom'if a*b > c*d else'TelecomParisTech'if a*b < c*d else'Tie')
