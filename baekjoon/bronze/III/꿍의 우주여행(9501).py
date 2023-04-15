for _ in ' '*int(input()):
    n, d = map(int, input().split())
    x = 0
    for _ in ' '*n:
        v, f, c = map(int, input().split())
        x += v*f/c >= d
    print(x)
