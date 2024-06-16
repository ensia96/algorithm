for l in [*open(0)][1:]:
    l = l.lower()
    x = sum(map(str.isalpha, l))
    y = sum(map(l.count, 'aeiou'))
    print(x-y, y)
