import heapq as h
A, *L = open(0)
n, m = map(int, A.split())
C = [[]for _ in ' '*-~n]
for l in L:
    i, j, w = map(int, l.split())
    C[i] += (w, j),
    C[j] += (w, i),
A, Q, V = [], [(0, 1, 1)], [0]*-~n
while Q:
    w, i, _ = h.heappop(Q)
    if V[i]:
        continue
    V[i], A = 1, A+[w]
    if len(A) == n-1:
        break
    for w, j in C[i]:
        h.heappush(Q, (w, j, i))
print(sum(A))
