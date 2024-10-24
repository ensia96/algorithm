for l in [*open(0)][1:]:
    x = sum(map(int, l.split()))
    print(x * x * ~-x // 2)
