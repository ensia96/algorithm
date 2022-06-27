n, k = map(int, input().split())
A = []
for _ in ' '*n:
    t = 0
    for i in input():
        t |= 1 << ord(i)-97
    A += t,
if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    def f(x, y, z):
        if y == k:
            return sum(z & a == a for a in A)
        t = 0
        for i in range(x, 26):
            if not z & 1 << i:
                t = max(t, f(i, y+1, z | 1 << i))
        return t
    print(f(0, 5, 532741))
