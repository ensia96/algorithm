for l in [*open(0)][:-1]:
    x = eval(l.replace(*'W-').replace(*'D+'))
    print([x, 'Not allowed'][x < -200])
