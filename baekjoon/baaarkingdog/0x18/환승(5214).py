import sys
I = sys.stdin.readline
n, k, m = map(int, I().split())
L, A = [[]for _ in ' '*(n+1)], 10**11
for i in range(m):
    I = [*map(int, I().split())]
    L += [I]
    for s in I:
        L[s] += [n+i+1]
Q, V = [(1, 1)], [0, 1]+[0]*(n+m-1)
for i, d in Q:
    if i == n:
        A = min(A, d)
    for s in L[i]:
        if not V[s]:
            Q += [(s, d+(s <= n))]
            if s <= n:
                V[s] = 1
print([A, -1][A == 10**11])
