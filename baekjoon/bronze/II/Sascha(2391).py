i = input
for _ in ' '*int(i()):
    a = i()
    x = int(i())
    r = map(i, ' '*x)
    print(min(r, key=lambda w: sum(x != y for x, y in zip(a, w))))
