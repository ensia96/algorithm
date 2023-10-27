n, m, *A = map(int, open(0).read().split())
x = y = 0
for a in A:
    if y+a > m:
        x += 1
        y = 0
    y += a
    print(x)
