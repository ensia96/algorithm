import sys
i = sys.stdin.readline
x, d = lambda: map(int, i().split()), {}
n, c = x()
l = [*x()]

for i in range(n):
    d[l[i]] = d.get(l[i], [0, n])
    d[l[i]][0] += 1
    d[l[i]][1] = min(d[l[i]][1], i)
print(*[k for k in sorted(d, key=lambda x: (-d[x][0], d[x][1]))
      for _ in range(d[k][0])])
