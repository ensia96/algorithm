_, A = open(0).read().split()
D = {}
T = 'BSA'
for t in T:
    c = A.count(t)
    D[c] = D.get(c, '')+t
t = D[max(D)]
print([t, 'SCU'][t == T])
