for l in [*open(0)][1:]:
    print('skipped'if '=' in l else eval(l))
