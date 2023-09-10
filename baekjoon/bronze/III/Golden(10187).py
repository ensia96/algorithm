x = 1.61803399
y = 0.01*x
for _ in ' '*int(input()):
    print(['not', 'golden'][x-y <= eval(input().replace(*' /')) <= x+y])
