x = 0
for a in map(int, open(0).read().split()[1:]):
    if x:
        y = 1
        for i in range(a):
            y = y*x % 10
        print(y or 10)
        x = 0
    else:
        x = a
