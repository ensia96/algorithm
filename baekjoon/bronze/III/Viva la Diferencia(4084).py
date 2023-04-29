for l in [*open(0)][:-1]:
    a, b, c, d = map(int, l.split())
    x = 0
    while 1:
        if a == b == c == d:
            break
        a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
        x += 1
    print(x)
