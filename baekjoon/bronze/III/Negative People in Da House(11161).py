for _ in ' '*int(input()):
    a = b = 0
    for _ in ' '*int(input()):
        x, y = map(int, input().split())
        a += y-x
        b = max(a, b)
    print(b)
