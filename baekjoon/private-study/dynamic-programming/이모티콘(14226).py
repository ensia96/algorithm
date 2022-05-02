s = int(input())
D = [[-1]*-~s for _ in ' '*-~s]
Q = [(1, 0)]
D[1][0] = 0
for q, c in Q:
    if D[q][q] < 0:
        D[q][q] = D[q][c]+1
        Q += (q, q),
    if q+c <= s and D[q+c][c] < 0:
        D[q+c][c] = D[q][c]+1
        Q += (q+c, c),
    if q > 1 and D[q-c][c] < 0:
        D[q-1][c] = D[q][c]+1
        Q += (q-1, c),
print(min(D[s][i]for i in range(-~s)if D[s][i] > 0))
