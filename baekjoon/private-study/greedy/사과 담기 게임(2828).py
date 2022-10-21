n, m = map(int, input().split())
a, b = 0, 1
for _ in ' '*int(input()):
    x, t = int(input()), 0
    if x < b:
        t = abs(x-b)
        b -= t
    elif b+m-1 < x:
        t = abs(x-b-m+1)
        b += t
    a += t
print(a)
