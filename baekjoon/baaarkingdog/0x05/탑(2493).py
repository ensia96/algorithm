import sys

n, t = int(input()), [*map(int, sys.stdin.readline().split()[::-1])]
a, i, m, r = [], 0, 10e8, 0

while t:
    c = t.pop()
    if c < m:
        m, r = c, i
    a.append(r)
    i += 1

print(*map(str, a))
