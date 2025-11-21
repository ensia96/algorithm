for l in [*open(0)][1:]:
    n, *R = map(int, l.split())
    print(*["NOT", "SAFE"][len({*R[::2]}) == n == len({*R[1::2]}):])
