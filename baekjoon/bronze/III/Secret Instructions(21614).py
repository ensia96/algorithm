t = ''
for l in [*open(0)][:-1]:
    x, y = divmod(int(l), 1000)
    x = sum(divmod(x, 10))
    t = [t, 'rliegfhtt'[x % 2::2]][x > 0]
    print(t, y)
