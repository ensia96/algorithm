for i in [*open(0)][1:]:
    print('YNEOS'[(n := int(i)) != n*n % 10**~-len(i)::2])
