for l in [*open(0)][1:]:
    print(int(str(sum(map(int, (i[::-1] for i in l.split()))))[::-1]))
