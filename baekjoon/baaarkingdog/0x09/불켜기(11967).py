import sys
import collections as c
i, r = sys.stdin.readline, range
l, d, q = lambda: map(int, i().split()), c.defaultdict(list), c.deque([(1, 1)])
n, m = l()
g, v = [[0] * (n+1) for _ in r(n+1)], [[0] * (n+1) for _ in r(n+1)]

for _ in r(m):
    x, y, a, b = l()
    c = (x, y)
    d[c].append((a, b))

g[1][1], v[1][1], c = 1, 1, 1

while q:
    a, b = q.popleft()
    for x, y in d[(a, b)]:
        if not g[x][y]:
            g[x][y], c = 1, c+1
            for i, j in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 < i <= n and 0 < j <= n and v[i][j]:
                    q.append((i, j))
    for x, y in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
        if 0 < x <= n and 0 < y <= n and g[x][y] and not v[x][y]:
            q.append((x, y))
            v[x][y] = 1
print(c)

# 풀이 참고 : https://chelseashin.tistory.com/91
