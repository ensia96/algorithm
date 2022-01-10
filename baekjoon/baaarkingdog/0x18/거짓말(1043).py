l, a = lambda i: map(int, i.split()), 0
x, y, *z = open(0)
n, m = l(x)
T, P = {*[*l(y)][1:]}, [{*[*l(i)][1:]}for i in z]
for _ in ' '*m:
    for p in P:
        T |= p & T and p
print(sum(not p & T for p in P))
