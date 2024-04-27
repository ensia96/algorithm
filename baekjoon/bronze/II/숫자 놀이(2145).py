for i in [*open(0)][:-1]:
    while len(i) > 1:
        i = str(sum(map(int, i.strip())))
    print(i)
