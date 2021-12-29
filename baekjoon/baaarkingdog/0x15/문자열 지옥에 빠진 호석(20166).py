import collections as c
n, m, k = map(int, input().split())
A, D, R = [input()for _ in ' '*n], c.defaultdict(int), range
for i in R(n):
    for j in R(m):
        Q = [(i, j, 1, A[i][j])]
        D[A[i][j]] += 1
        for x, y, d, s in Q:
            if d == 5:
                continue
            for a, b in [((x+p-1) % n, (y+q-1) % m)for p in R(3)for q in R(3)if (p, q) != (1, 1)]:
                D[s+A[a][b]] += 1
                Q += [(a, b, d+1, s+A[a][b])]
for _ in ' '*k:
    print(D.get(input(), 0))
