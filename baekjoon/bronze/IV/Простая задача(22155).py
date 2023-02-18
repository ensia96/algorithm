for _ in ' '*int(input()):
    i, f = map(int, input().split())
    print('YNeos'[i*f > 2::2])
