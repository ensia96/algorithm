_, *L = open(0, 'rb')
while L:
    _, l, j, *L = L
    print(''.join(chr((c + 7 + j[0] - l[0]) % 26 + 97)for c in l[:-1]))
