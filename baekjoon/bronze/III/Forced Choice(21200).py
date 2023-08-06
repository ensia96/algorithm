I, *L = open(0)
_, p, _ = I.split()
for l in L:
    print(['REMOVE', 'KEEP'][p in l.split()[1:]])
