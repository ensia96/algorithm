for L in [*open(0)][:-1]:
    a = b = c = 0
    d, *l = map(int, L.split())
    while c < d:
        if a > b:
            b += l[d := d - 1]
        else:
            a += l[(c := c + 1) - 1]
    print(['No equal partitioning.',
          f'Sam stops at position {c} and Ella stops at position {d + 1}.'][a == b])
