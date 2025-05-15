D = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
for l in [*open(0)][:-1]:
    a, b = l.split()
    a = int(a)
    print(''.join(D[(D.find(i)+a) % 28]for i in b[::-1]))
