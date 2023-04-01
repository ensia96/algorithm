for l in open(0):
    a, b, c = map(int, l.split())
    if a+b+c:
        x = (c == 2*b-a)+2*(c == b**2//a)
        print(' AG'[x]+'P', [0, 2*c-b, c**2//b][x])
