for l in open(0).read().split()[:-1]:
    A = B = x = y = 0
    for i in l:
        if 'A' == i:
            x += 1
            if x > 3 and x-y > 1:
                A += 1
                x = y = 0
        else:
            y += 1
            if y > 3 and y-x > 1:
                B += 1
                x = y = 0
    print('A', A, 'B', B)
