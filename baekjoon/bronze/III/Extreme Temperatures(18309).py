t = []
for l in open(0):
    t += l.split()[1:]
*t, = map(int, t)
print(min(t), max(t))
