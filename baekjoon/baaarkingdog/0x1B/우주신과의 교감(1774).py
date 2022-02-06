import heapq as h
l, t = lambda: map(int, input().split()), lambda a, b: (a**2+b**2)**.5
n, m = l()
n += 1
D = [[0]*n for _ in ' '*n]
L = {i: (*l(),)for i in range(1, n)}
for i in range(1, n):
    for j in range(1, n):
        if i == j:
            continue
        a, b = L[i]
        c, d = L[j]
        D[i][j] = t(a-c, b-d)
for _ in ' '*m:
    i, j = l()
    D[i][j] = D[j][i] = 0
Q, V = [(0, 1)], [0]*n
A = E = 0
while Q:
    w, i = h.heappop(Q)
    if V[i]:
        continue
    V[i], A, E = 1, A+w, E+1
    if E == n-1:
        break
    for j in range(1, n):
        h.heappush(Q, (D[i][j], j))
print(f"{A:.2f}")
