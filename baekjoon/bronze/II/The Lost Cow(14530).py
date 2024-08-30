x, y = map(int, input().split())
a, c = 0, x
d = s = p = 1
while 1:
    for _ in " " * d:
        c += s
        a += 1
        c == y and exit(print(a))
    p *= 2
    d = abs(c - x) + p
    s *= -1
