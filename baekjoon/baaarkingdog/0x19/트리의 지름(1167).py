import sys
I = sys.stdin.readline
n = int(I())
A, C, D = 0, [{}for _ in ' '*-~n], [0]*-~n
for _ in ' '*n:
    i, *c = map(int, I().split())
    for j, w in zip(c[0:-1:2], c[1::2]):
        C[i][j] = w
q, v = [1], [0, 1]+[0]*~-n
for p in q:
    for c in C[p]:
        if not v[c]:
            v[c] = C[c].pop(p)
            q += c,
for p in q[::-1]:
    for c in C[p]:
        x, y = D[p], D[c]+C[p][c]
        A, D[p] = max(A, x+y), max(x, y)
print(A)
