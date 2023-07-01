x = 1
T = []
for l in [*open(0)][:-1]:
    p, s = map(int, l.split())
    T += f"Hole #{x}\n{[['Par','Bordie',['Eagle','Hole-in-one'][s<2],'Double Eagle','Bogey'][p-s],'Double Bogey'][p-s<-1]}.",
    x += 1
print('\n\n'.join(T))
