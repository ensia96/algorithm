for _ in ' '*int(input()):
    i, f = map(int, input().split())
    print('YNeos'[(i*f > 2)*(i < 3)*(f < 3)::2])
