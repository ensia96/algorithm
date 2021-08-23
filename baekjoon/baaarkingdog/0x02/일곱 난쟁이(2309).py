l = sorted([*map(int, [*open(0)])])
r, d = len(l), sum(l) - 100

for i in range(r):
    for j in range(r):
        if i != j and l[i] + l[j] == d:
            l[i] = l[j] = 0
            break

print("\n".join(map(str, filter(None, l))))
