for l in [*open(0)][1:]:
    s = l[:-1].lower()
    print('YNeos'[s != s[::-1]::2])
