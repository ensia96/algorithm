C = open(0).read().count
for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
    c = C(i)
    c and print(i, c)
