T = []
for l in [*open(0)][1:]:
    a, b, c, *D = l.split()
    T += (int(a), int(b), int(c), D),
print(*max(T)[-1])
