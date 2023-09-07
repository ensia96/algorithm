D = {'y': 'a', 'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'y',
     'Y': 'A', 'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'Y'}
for l in [*open(0)][1:]:
    print(''.join(D[i]if i in D else i for i in l.strip()))
