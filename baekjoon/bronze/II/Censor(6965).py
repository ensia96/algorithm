for l in [*open(0)][1:]:
    print(*[[i, "*" * 4][len(i) == 4] for i in l.split()])
    print()
