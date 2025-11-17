I = input
while n := int(I()):
    L = [I()for _ in ' ' * n]
    x = min(map(len, L))
    print(min([i for i in range(x)if len({l[i:]for l in L}) < n] + [x]) - 1)
