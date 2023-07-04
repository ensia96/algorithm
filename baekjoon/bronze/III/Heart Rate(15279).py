for l in [*open(0)][1:]:
    x, y = map(float, l.split())
    x = int(x)
    print(60*~-x/y, 60*x/y, 60*-~x/y)
