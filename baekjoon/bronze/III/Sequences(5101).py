for l in [*open(0)][:-1]:
    a, b, c = map(int, l.split())
    x = c-a
    print([x//b+1, 'X'][x % b or x//b < 0])
