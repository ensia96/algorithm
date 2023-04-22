for l in [*open(0)][1:]:
    print(+(bin(int(l)).count('1') < 2))
