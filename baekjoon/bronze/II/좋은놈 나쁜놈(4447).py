for i in [*open(0)][1:]:
    g, b = map(i.lower().count, 'gb')
    print(i[:-1], 'is', ['NEUTRAL', 'GOOD', 'A BADDY'][(g > b)+2*(g < b)])
