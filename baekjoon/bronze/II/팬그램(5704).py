for l in [*open(0)][:-1]:
    print('NY'[len(set(l.lower())-{*'\n '}) > 25])
