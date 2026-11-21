_, *f = open(0)
d = {}
for s in f:
    if ' ' in s:
        k = s[0] + s.split()[1][0]
        d[k] = [s[:-1], 'ambiguous'][k in d]
    else:
        print(d.get(s[:2], 'nobody'))

