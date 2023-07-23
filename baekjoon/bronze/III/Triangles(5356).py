t = []
for l in [*open(0)][1:]:
    x, y = l.split()
    t += '\n'.join([chr(65+-~i*(ord(y)+i-65) % 26)for i in range(int(x))]),
print('\n\n'.join(t))
