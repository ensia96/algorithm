a, b, c, d, e = map(int, open(0))
N = B = 0
x, y = a, c
while e:
    if x > 0:
        N += 1
        x = [x-1, -b][x == 1]
    else:
        N -= 1
        x = [x+1, a][x == -1]
    if y > 0:
        B += 1
        y = [y-1, -d][y == 1]
    else:
        B -= 1
        y = [y+1, c][y == -1]
    e -= 1
print(['NBiykrkoyn'[N < B::2], 'Tie'][N == B])
