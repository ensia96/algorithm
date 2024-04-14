for l in [*open(0)][:-1]:
    print(l.lower().count('nemo') and 'Found' or 'Missing')
