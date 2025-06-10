for l in [*open(0)][:-1]:
    print(int(f"{int(l):032b}"[::-1], 2))
