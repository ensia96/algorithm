for _ in ' '*int(input()):
    a, b, c, d = map(int, input().split())
    x = sum([b, c, d])
    print(a, x, 'FPAAISLS'[(x > 54)*(b > 10)*(c > 7)*(d > 11)::2])
