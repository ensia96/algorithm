for l in [*open(0)][1:]:
    print('ABCDCB'[~-int(l) % 6])
