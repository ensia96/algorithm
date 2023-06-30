for l in [*open(0)][:-1]:
    n = int(l)
    if n in [1916, 1940, 1944]:
        print(n, 'Games cancelled')
    elif n % 4 < 1:
        print(n, ['Summer Olympics', 'No city yet chosen'][n > 2020])
    else:
        print(n, 'No summer games')
