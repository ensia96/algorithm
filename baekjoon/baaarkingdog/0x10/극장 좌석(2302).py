i, a, c = lambda: int(input()), 1, 0
n, m, d = i(), i(), [0, 1, 2, 3]
l, _ = [0]*(n+1)+[1], [d.append((d[i-2]*2)+d[i-3]) for i in range(4, n+1)]
for _ in range(m):
    l[i()] = 1
for i in range(1, n+2):
    a, c = [a, a*d[c]][l[i]], [c+1, 0][l[i]]
print(a)
