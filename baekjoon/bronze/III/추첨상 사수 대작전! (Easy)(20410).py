m, s, x, y = map(int, input().split())
M = range(m)
for a in M:
    for c in M:
        x == (a*s+c) % m and y == (a*x+c) % m and exit(print(a, c))
