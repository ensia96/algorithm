import sys
i = sys.stdin.readline
n, l = int(i()), []
a = c = 0
while n:
    s, e = map(int, i().split())
    l += [(e, -1), (s, 1)]
    n -= 1
for _, f in sorted(l):
    c += f
    a = max(a, c)
print(a)
