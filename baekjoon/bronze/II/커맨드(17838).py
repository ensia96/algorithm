for l in [*open(0)][1:]:
    print(+("!!??!??\n" == l.replace(l[0], "!").replace(l[2], "?")))
