for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    t = -((9000 - a * 15 - b * 20 - c * 25) // -40)
    print([t, "impossible"][t > 100])
