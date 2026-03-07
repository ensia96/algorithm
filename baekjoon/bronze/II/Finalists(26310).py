n, *L = open(0)
print((int(n) + [l[0]for l in sorted(L, key=lambda l: eval(
    '3*%s+7*%s+12*%s+28*%s+15*%s' % (*l.split()[1:],)))].index('T')) // 6)
