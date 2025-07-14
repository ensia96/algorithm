for _ in ' '*int(input()):
    l, r, s = map(int, input().split())
    x = y = 1
    while 1:
        t, x = [(s-x, x+1), (s+x, x)][y % 2]
        if t in [l, r]:
            break
        y += 1
    print(y+1)
