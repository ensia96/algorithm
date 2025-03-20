_, _, *T = [int(i[-2]) for i in open(0)]
for t in T:
    _ ^= t
print(_)
