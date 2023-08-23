for l in [*open(0)][1:]:
    y, m, d = map(int, l.split())
    print(
        'YNeos'[not (y < 1989 or (y == 1989 and (m < 2 or (m == 2 and d <= 27))))::2])
