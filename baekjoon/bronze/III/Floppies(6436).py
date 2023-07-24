x, A = 1860000, []
for l in [*open(0)][:-1]:
    i = int(l)
    i = i//2+i % 2
    i += i//2
    A += f'File #{len(A)+1}\nJohn needs {(i+x-1)//x} floppies.',
print('\n\n'.join(A))
