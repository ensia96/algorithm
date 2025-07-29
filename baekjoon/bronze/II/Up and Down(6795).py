a, b, c, d, e = map(int, open(0))
N = B = 0
x, y = a, c
while e:
    if x > 0:
        N += 1
        x -= 1
        if x == 0:
            x = -b
    else:
        N -= 1
        x += 1
        if x == 0:
            x = a
    if y > 0:
        B += 1
        y -= 1
        if y == 0:
            y = -d
    else:
        B -= 1
        y += 1
        if y == 0:
            y = c
    e -= 1
print(['NBiykrkoyn'[N < B::2], 'Tie'][N == B])
