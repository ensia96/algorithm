for l in [*open(0)][:-1]:
    i, l = l.split()
    print(int(l.replace(i, '') or 0))
