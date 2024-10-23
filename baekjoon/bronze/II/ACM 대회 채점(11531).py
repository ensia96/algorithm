D = {}
i = j = 0
for l in [*open(0)][:-1]:
    t, p, r = l.split()
    D[p] = (D.get(p, []) + int(t),)
    if "t" in r:
        i += 1
        j += 20 * ~-len(D[p]) + D[p][-1]
print(i, j)
