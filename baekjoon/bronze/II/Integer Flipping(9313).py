for l in [*open(0)][:-1]:
    print(int(bin(int(l))[2:].rjust(32, '0')[::-1], 2))
