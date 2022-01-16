import sys
L, n = lambda: map(int, sys.stdin.readline().split()), 0
n, m = L()
n += 1
P, D = [0]+[*L()], [0]*n
for _ in ' '*m:
    i, w = L()
    D[i] += w
for i in range(2, n):
    D[i] += D[P[i]]
print(*D[1:])
