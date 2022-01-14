l, a = lambda: map(int, input().split()), 0
n, m = l()
n += 1
T = [0]*n
for i in [*l()][1:]:
    T[i] = 1
P = [[*l()][1:]for _ in ' '*m]
for p in P:
    for i in p:
        if T[i]:
            break
    else:
        continue
    for i in p:
        T[i] = 1
for p in P:
    for i in p:
        if T[i]:
            break
    else:
        a += 1
print(a)
