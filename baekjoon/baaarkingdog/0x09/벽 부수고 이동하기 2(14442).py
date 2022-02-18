import collections as c
M = 2**20
n, m, k = map(int, input().split())
B = [[*map(int, input())]for _ in ' '*n]
D = [[[M]*-~k for _ in ' '*m]for _ in ' '*n]
R, Q = lambda x, y: 0 <= x < n and 0 <= y < m, c.deque((1, 0, 0, 0),)
while Q:
    d, i, j, h = Q.popleft()
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if not R(x, y):
            continue
        z = h+B[x][y]
        if z > k:
            continue
        if D[x][y][z] > d+1:
            D[x][y][z] = d+1
            Q += [(d+1, x, y, z)]
A = min(D[-1][-1])
print(-(A == M) or A)
