for _ in ' '*int(input()):
    a, b, c, d = map(int, input().split())
    print('Eurecom'if a*c > b*d else'TelecomParisTech'if a*c < b*d else'Tie')
