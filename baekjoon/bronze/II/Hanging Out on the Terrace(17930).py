l, *L = open(0)
x = y = 0
n, m = map(int, l.split())
for l in L:
    a, b = l.split()
    b = int(b)
    if 'e' == a[0]:
        if x + b > n:
            y += 1
        else:
            x += b
    else:
        x -= b
print(y)
