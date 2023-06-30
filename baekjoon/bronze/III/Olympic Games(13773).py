for l in [*open(0)][:-1]:
    n = int(l)
    if 1914 <= n <= 1918 or 1939 <= n <= 1945:
        print(n, 'Games cancelled')
    elif n > 2016:
        print(n, 'No city yet chosen')
    elif n % 4 == 0:
        print(n, 'Summer Olympics')
    else:
        print(n, 'No summer games')
