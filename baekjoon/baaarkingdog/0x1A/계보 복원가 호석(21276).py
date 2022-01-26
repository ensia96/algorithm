I = input
n, D = int(I()), {i: [0, [], []] for i in I().split()}
for _ in ' '*int(I()):
    x, y = I().split()
    D[y][1] += [x]
    D[x][0] += 1
Q = [k for k in D if not D[k][0]]
print(len(Q))
print(*sorted(Q))
for x in Q:
    for y in D[x][1]:
        D[y][0] -= 1
        if not D[y][0]:
            Q += [y]
            D[x][2] += [y]
for k in sorted(D):
    L = D[k][2] or D[k][1]
    print(k, len(L), *sorted(L))
