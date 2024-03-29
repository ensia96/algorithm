for l in [*open(0)][1:]:
    x, y = l.split('-')
    s = 0
    for i in x:
        s = (s+ord(i)-65)*26
    print(*[['not'], []][abs(s//26-int(y)) > 100], 'nice')
