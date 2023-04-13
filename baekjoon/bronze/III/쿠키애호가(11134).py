for l in [*open(0)][1:]:
    x, y = divmod(*map(int, l.split()))
    print(x+(y > 0))
