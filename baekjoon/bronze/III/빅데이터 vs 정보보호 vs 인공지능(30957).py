_, A = open(0).read().split()
D = {}
T = 'BSA'
for t in T:
    D[c] = D.get(A.count(t), '')+t
t = D[max(D)]
print([t, 'SCU'][t == T])
