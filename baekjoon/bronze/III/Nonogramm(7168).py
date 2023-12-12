_, _, *A = open(0).read().split()
for a in A+[''.join(i)for i in zip(*A)]:
    x, y, z = '.', 0, []
    for i in a+'.':
        if i == '#':
            y += 1
        elif y > 0:
            z += y,
            y = 0
    print(*(z or [0]))
