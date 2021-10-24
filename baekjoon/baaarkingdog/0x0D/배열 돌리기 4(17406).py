from itertools import permutations as P
L, R = lambda: map(int, input().split()), range
n, m, k = L()
A, B, C = 5001, [[*L()]for _ in R(n)], [[*L()]for _ in R(k)]
for p in P(R(k), k):
    b = [[B[y][x]for x in R(m)]for y in R(n)]
    for K in p:
        r, c, S = C[K]
        r, c, q = r-1, c-1, []
        for s in R(S, 0, -1):
            q += [(r-s, i+1, b[r-s][i])for i in R(c-s, c+s)]
            q += [(i+1, c+s, b[i][c+s])for i in R(r-s, r+s)]
            q += [(r+s, i-1, b[r+s][i])for i in R(c+s, c-s, -1)]
            q += [(i-1, c-s, b[i][c-s])for i in R(r+s, r-s, -1)]
        for y, x, v in q:
            b[y][x] = v
    A = min(*map(sum, b), A)
print(A)
