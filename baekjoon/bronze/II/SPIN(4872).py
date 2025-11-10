l, *L = open(0)
*D, = map(int, l[:-1])
for l in L:
    *D, = map(sum, zip(D, map(int, l)))
print(*[d % 10 for d in D], sep='')
