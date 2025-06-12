t = ''
for a in input():
    t += 'SKH'['RBL'.index(a)]
    if t[-3:] in ["SKH", "SHK", "KSH", "KHS", "HSK", "HKS"]:
        t = t[:-3]+'C'
print(t)
