for l in [*open(0)][:-1]:
    print(len({i.lower()for i in l if i.isalpha()}))
