for l in [*open(0)][1:]:
    x = sum(ord(i)-64 for i in ''.join(l.split()))
    print([x, 'PERFECT LIFE'][x == 100])
