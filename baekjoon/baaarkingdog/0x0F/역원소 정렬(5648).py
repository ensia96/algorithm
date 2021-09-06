n = []
for l in open(0):
    n += l.split()
print(*sorted(map(int, [i[::-1] for i in n[1:]])))
