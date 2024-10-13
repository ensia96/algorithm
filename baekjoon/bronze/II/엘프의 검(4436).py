for i in map(int, open(0)):
    N = {*range(10)}
    x = 1
    while len(N):
        N -= {*map(int, str(i * x))}
        x += 1
    print(x - 1)
