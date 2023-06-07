for l in [*open(0)][1:]:
    print(l.strip(), ['Check', 'Seems OK'][sum(map(int, l.split())) == 180])
