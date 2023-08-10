for l in [*open(0)][1:]:
    l = l.strip()
    print(l+'.'*(l[-1] != '.'))
