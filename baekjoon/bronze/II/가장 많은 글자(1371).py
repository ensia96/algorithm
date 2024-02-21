A = open(0).read().count
T = ['']*2501
for i in range(26):
    a = chr(i+97)
    T[A(a)] += a
print([t for t in T if t][-1])
