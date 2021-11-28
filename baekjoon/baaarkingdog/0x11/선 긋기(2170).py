import sys
I = sys.stdin.readline
l = sorted((*map(int, I().split()),)for _ in ' '*int(I()))
a, s, e = 0, *l[0]
for x, y in l:
    a, s, e = [(a, s, max(e, y)), (a+e-s, x, y)][e < x]
print(a+e-s)
