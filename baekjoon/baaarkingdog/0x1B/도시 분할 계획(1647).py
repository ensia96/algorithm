import heapq as h
A, *L = open(0)
n, m = map(int, A.split())
C = [[]for _ in ' '*-~n]
for l in L:
    i, j, w = map(int, l.split())
    C[i] += (w, j),
    C[j] += (w, i),
Q, V = [(0, 1)], [0]*-~n
A = E = 0
while Q:
    w, i = h.heappop(Q)
    if V[i]:
        continue
    V[i], A, E = 1, A+w, E+1
    if not E-n+1:
        break
    for w, j in C[i]:
        h.heappush(Q, (w, j))
print(A)
