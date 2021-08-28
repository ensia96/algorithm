import sys
import collections as c

i = sys.stdin.readline
q, d = c.deque(), [(1, 0), (0, 1), (-1, 0), (0, -1)]

r, c = map(int, i().split())
b = [[*i().strip()] for _ in range(r)]
a = s = 'IMPOSSIBLE'

for n in range(r):
    for m in range(c):
        if b[n][m] == 'J':
            b[n][m] = 0
            j = (n, m)
        if b[n][m] == 'F':
            b[n][m] = 0
            q.append((n, m))

while q:
    n, m = q.popleft()
    for x, y in d:
        v, w = n + y, m + x
        if 0 <= v < r and 0 <= w < c and b[v][w] == '.':
            b[v][w] = b[n][m] + 1
            q.append((v, w))

q.append(j)

while q:
    if a != s:
        break
    n, m = q.popleft()
    f = b[n][m]
    for x, y in d:
        v, w = n + y, m + x
        if 0 <= v < r and 0 <= w < c:
            e = b[v][w]
            if e != '#':
                if f == '.' or f + 1 < e:
                    b[v][w] = f + 1
                    q.append((v, w))
        else:
            a = f + 1
            break

print(a)
