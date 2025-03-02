for l in [*open(0)][1:]:
    print(~-min(map(int, l.split())) * 2)
