for l in [*open(0)][:-1]:
    x, y = map(int, l.split())
    i = j = 0
    while x*y:
        x, a = divmod(x, 10)
        y, b = divmod(y, 10)
        j = a+b+j > 9
        i += j
    print(i+max(x, y) % 10+j > 9)
