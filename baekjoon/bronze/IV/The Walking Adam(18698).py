for _ in ' '*int(input()):
    x = 0
    for i in input():
        x += 1-2*(i == 'D')
        x += (x < 0)
    print(x)
