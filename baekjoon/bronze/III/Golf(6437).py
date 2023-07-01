x = 1
T = []
for l in [*open(0)][:-1]:
    p, s = map(int, l.split())
    T += f"Hole #{x}\n{[[['Par','Birdie','Eagle','Double eagle','Bogey'][p-s],'Hole-in-one'][s<2],'Double Bogey'][-2<p-s<4]}.",
    x += 1
print('\n\n'.join(T))
