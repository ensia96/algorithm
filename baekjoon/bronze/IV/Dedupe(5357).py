for _ in ' '*int(input()):
    a = input()
    x = y = a[0]
    for i in range(len(a)):
        if x != a[i]:
            x = a[i]
            y += x
    print(y)
