import sys
i = sys.stdin.readline
l, _ = lambda: sorted([*map(int, i().split())]), 0

for _ in range(int(i())):
    i()
    a, b = l(), l()
    _ = p = q = 0
    v, w = len(a), len(b)
    while 1:
        q = d = 0
        c = p
        if v == p or w == q:
            break
        while q < w and b[q] < a[p]:
            q += 1
            d += 1
        while p < v and a[c] == a[p]:
            p += 1
        _ += (p-c)*d
    print(_)
