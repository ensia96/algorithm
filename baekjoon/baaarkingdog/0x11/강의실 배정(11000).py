import sys
i = sys.stdin.readline
N, l = int(i()), []
a = c = 0
while N:
    s, e = map(int, i().split())
    l += [(e, -1), (s, 1)]
    N -= 1
for s, e in sorted(l):
    c += e
    a = max(a, c)
print(a)
