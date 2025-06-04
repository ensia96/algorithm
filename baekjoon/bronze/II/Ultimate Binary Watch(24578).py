for a, b, c, d in zip(*[['.*'[int(x)]for x in bin(int(i))[2:].rjust(4, '0')]for i in input()]):
    print(a, b, ' ', c, d)
