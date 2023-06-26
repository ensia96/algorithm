i, A = 1, []
for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    t = 'no '*(a <= b)+'drought'
    while a/5 > b:
        b *= 5
        t = 'mega '+t
    A += f'Data Set {i}:\n'+t,
    i += 1
print('\n\n'.join(A))
