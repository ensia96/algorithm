for _ in '   ':
    l = input()
    x = y = 1
    for i in range(7):
        if l[i] == l[i+1]:
            x += 1
        else:
            x, y = 1, max(x, y)
    print(y)
