for l in open(i := 0):
    'E' in l and exit()
    i += 1
    print(f'Case {i}: {str(eval(l)).lower()}')
