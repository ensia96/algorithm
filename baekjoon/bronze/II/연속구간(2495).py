for l in open(0):
    x = y = 1
    for i in range(7):
        x = x*(l[i] == l[i+1])+1
        y = max(x, y)
    print(y)
