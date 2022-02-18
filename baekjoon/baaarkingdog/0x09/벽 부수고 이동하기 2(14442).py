M = 2**20
n, m, k = map(int, input().split())
B = [[*map(int, input())]for _ in ' '*n]
D = [[[M]*-~k for _ in ' '*m]for _ in ' '*n]
V = [[[0]*-~k for _ in ' '*m]for _ in ' '*n]
R, Q = lambda x, y: 0 <= x < n and 0 <= y < m, [(1, 0, 0, 0)]
for d, i, j, h in Q:
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if not R(x, y):
            continue
        z = h+B[x][y]
        if z > k:
            continue
        D[x][y][z] = min(d+1, D[x][y][z])
        if not V[x][y][z]:
            V[x][y][z] = 1
            Q += [(d+1, x, y, z)]
A = min(D[-1][-1])
print(-(A == M) or A)
