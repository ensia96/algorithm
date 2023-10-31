_, *A = open(0).read().split()
for a in A:
    print(min(map(a.count, 'ab')))
