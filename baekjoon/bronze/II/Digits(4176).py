while (l := input()) != 'END':
    t = ['1', l]
    while t[-1] != t[-2]:
        t += str(len(t[-1])),
    print(len(t)-1-(t[0] != t[1]))
