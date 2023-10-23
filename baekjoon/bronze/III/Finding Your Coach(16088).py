for _ in ' '*int(input()):
    a, b, c, d = map(int, input().split())
    x = abs(c-d)
    print('G'if c == d else 'L'if (x <= a)*(x > b)
          else 'R'if (x <= b)*(x > a)else 'E')
