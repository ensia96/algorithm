_, x, *L = map(int, open(0).read().split())
for i in L:
    if x == 0:
        x = i
    elif i % x == 0:
        x = 0
        print(i)
