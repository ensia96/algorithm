t = []
for l in open(0):
    a, *_, b = sorted(map(int, l.split()[1:]+t))
    t = [a, b]
print(a, b)
