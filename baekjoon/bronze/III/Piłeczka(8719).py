for l in [*open(0)][1:]:
    x, y = map(int, l.split())
    t = 0
    while x*2**t < y:
        t += 1
    print(t)
