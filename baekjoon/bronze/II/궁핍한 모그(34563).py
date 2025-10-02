for l in [*open(0)][1:]:
    print(eval(l.replace(*' +')) - 1)
