*L, = open(0).read().split()
t, T = L[1], {}
for x, y in zip(L[::2], L[1::2]):
    if t == y:
        t = x
        T[t] = 1
print(t, len(T))
