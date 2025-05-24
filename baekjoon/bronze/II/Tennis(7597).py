while (l := input()) != '#':
    A = B = x = y = 0
    for i in l:
        x += 'A' == i
        y += 'B' == i
        if x > 3 and x-y > 1:
            A += 1
            x = y = 0
        if y > 3 and y-x > 1:
            B += 1
            x = y = 0
    print('A', A, 'B', B)
