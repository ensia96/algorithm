n, x, y, *A = open(0).read().split()
x, y = int(x), int(y)
for a, b in zip(A[::2], A[1::2]):
    l = len(a)
    b = (int(b)**l/l)**(1/l)
    i = j = 0
    if 'N' in a:
        j = b
    if 'E' in a:
        i = b
    if 'W' in a:
        i = -b
    if 'S' in a:
        j = -b
    x, y = x+i, y+j
print(x, y)
