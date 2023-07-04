for l in [*open(0)][1:]:
    print(int(str(eval(l[::-1].replace(*' +')))[::-1]))
