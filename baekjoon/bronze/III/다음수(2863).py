for l in [*open(0)][:-1]:
    a, b, c = map(int, l.split())
    x = (b-a and b-a == c-b)+2*(b*a and (b/a == c/b))
    print('GA'[-x]+'P', [b and c**2//b, 2*c-b][-x])
