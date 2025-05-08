_, a, _, *B = open(t := 0)
for b in B:
    x = sum(x == y for x, y in zip(a, b))
    if t < x:
        _, t = b, x
print(_[:-1])
