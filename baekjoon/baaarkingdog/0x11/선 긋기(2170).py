import sys
I = sys.stdin.readline
l = sorted((*map(int, I().split()),)for _ in ' '*int(I()))
a = 0
while 1:
    s, e = l.pop()
    if not l:
        exit(print(a+e-s))
    x, y = l.pop()
    if s <= y:
        l += [(min(s, x), e)]
    else:
        a, l = a+e-s, l+[(x, y)]
