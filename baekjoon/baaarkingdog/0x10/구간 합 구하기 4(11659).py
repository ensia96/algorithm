import sys
d, _ = lambda: [*map(int, sys.stdin.readline().split())], 0
n, m, *l = d()+d()

for _ in range(m):
    i, j = d()
    print(sum(l[i-1:j]))
