l = sorted([*map(int, [*open(0)])])
r, d, f = len(l), sum(l) - 100, 1

for i in range(r):
    for j in range(r):
        if i != j and l[i] + l[j] == d:
            l[i] = l[j] = f = 0
            print("\n".join(map(str, filter(None, l))))
            break
    if not f:
        break
