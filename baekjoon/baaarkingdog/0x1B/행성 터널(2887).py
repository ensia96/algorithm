import sys
import heapq as h
I = sys.stdin.readline
n = int(I())+1
P = [0]+[(*map(int, I().split()),)for _ in ' '*~-n]
Q, V = [(0, 1)], [0]*n
A = E = 0
while Q:
    w, i = h.heappop(Q)
    if V[i]:
        continue
    V[i], A, E, T = 1, A+w, E+1, []
    a, b, c = P[i]
    if E == n:
        break
    for j in range(1, n):
        if V[j]:
            continue
        x, y, z = P[j]
        T.append((min(abs(a-x), abs(b-y), abs(c-z)), j))
    T and h.heappush(Q, sorted(T)[0])
print(A)
