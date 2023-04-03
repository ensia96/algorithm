A = []
for i, l in enumerate([*open(0)][1:]):
    a, b, c = sorted(map(int, l.split()))
    A += f'Scenario #{i+1}:\n'+'yneos'[a*a+b*b != c*c::2],
print('\n\n'.join(A))
