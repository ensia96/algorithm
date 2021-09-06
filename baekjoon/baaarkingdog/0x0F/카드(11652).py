import sys
import collections as c

i, d = sys.stdin.readline, c.defaultdict(int)

for _ in range(int(i())):
    d[int(i())] += 1

print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])
