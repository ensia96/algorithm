x = 1.61803399
y = 0.01*x
for l in [*open(0)][1:]:
    print(['not', 'golden'][x-y <= eval(l.replace(*' /')) <= x+y])
