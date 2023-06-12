for _ in ' '*int(input()):
    a, b, c, x, y, z = map(int, input().split())
    print(c+abs(a-x)+abs(b-y)+z)
