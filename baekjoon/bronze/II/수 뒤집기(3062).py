for l in [*open(0)][1:]:
    s = str(int(l)+int(l[::-1]))
    print('YNEOS'[s != s[::-1]::2])
