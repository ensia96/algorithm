*L, = [*open(0)]
n = max(map(len, L))
print(sum((n - len(l))**2 for l in L[:-1]))
