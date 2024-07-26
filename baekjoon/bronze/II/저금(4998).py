for l in open(0):
    a, b, c = map(float, l.split())
    x = 0
    while a < c:
        a *= 1 + b / 100
        x += 1
    print(x)
