from collections import deque as q
n, c, d, q = int(input()), 0, 0, q([(0, 0)])
m, r = [[0]*n for _ in range(n)], {}
m[0][0], dy, dx = 2, [0, 1, 0, -1], [1, 0, -1, 0]

for _ in range(int(input())):
    i, j = map(int, input().split())
    m[i-1][j-1] = 1
for _ in range(int(input())):
    t, h = input().split()
    r[int(t)] = [1, -1][h == 'L']

while 1:
    hy, hx = q[0]
    my, mx = hy+dy[d], hx+dx[d]
    c += 1
    if n <= my or my < 0 or n <= mx or mx < 0 or m[my][mx] == 2:
        exit(print(c))
    if m[my][mx] != 1:
        ty, tx = q.pop()
        m[ty][tx] = 0
    q.appendleft((my, mx))
    m[my][mx] = 2
    if c in r:
        d = (d + r[c]) % 4
