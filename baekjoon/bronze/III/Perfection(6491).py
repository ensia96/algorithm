for i in map(int, open(0).read().split()[:-1]):
    x = sum(j for j in range(1, i)if not i % j)
    print(i, ['PERFECT', 'ABUNDANT', 'DEFICIENT'][(x > i)+2*(x < i)])
