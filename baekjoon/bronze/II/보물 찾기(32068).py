for _ in ' '*int(input()):
    l, r, s = map(int, input().split())
    x, y = s-l, r-s
    print([y*2, x*2+1][x < y])
