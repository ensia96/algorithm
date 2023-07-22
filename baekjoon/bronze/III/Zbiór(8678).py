for l in [*open(0)][1:]:
    print('TNAIKE'[eval('%'.join(l.split()[::-1])) > 0::2])
