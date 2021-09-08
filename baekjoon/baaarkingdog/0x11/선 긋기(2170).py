import sys
I = sys.stdin.readline
a = 0
s = e = int(-1e10)
for x, y in sorted((*map(int, I().split()),)for _ in ' '*int(I())):
    a, s, e = [(a, s, max(e, y)), (a+e-s, x, y)][e < x]
print(a+e-s)
