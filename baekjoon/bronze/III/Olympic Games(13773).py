for l in [*open(0)][:-1]:
    n = int(l)
    if 1915 < n < 1919 or 1938 < n < 1946:
        print(n, 'Games cancelled')
    elif n > 2020:
        print(n, 'No city yet chosen')
    elif n % 4 == 0:
        print(n, 'Summer Olympics')
    else:
        print(n, 'No summer games')
