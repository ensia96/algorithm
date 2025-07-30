for l in [*open(0)][1:]:
    x = y = 0
    z = l.count('?')
    for i in l:
        i, j = [(-1, 0), (1, 0), (0, 1), (0, -1), (0, 0)]['LRUD'.find(i)]
        x += i
        y += j
    print(x-z, y-z, x+z, y+z)
