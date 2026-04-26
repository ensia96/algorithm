for l in [*open(0)][1:]:
    a, b = l.split()
    print(-~-int(a) % ~-int(b))
