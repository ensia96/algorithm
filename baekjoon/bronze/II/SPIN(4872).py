D = [0] * 4
for l in open(0):
    *D, = map(sum, zip(D, map(int, l)))
print(*[d % 10 for d in D], sep='')
