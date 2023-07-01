x = 1
T = []
for l in [*open(0)][:-1]:
    p, s = map(int, l.split())
    g = p-s
    T += f"Hole #{x}\n{[['Par',[0,'Birdie','Eagle','Double eagle'][g],['Bogey','Double Bogey'][g<-1]][(g>0)+2*(g<0)],'Hole-in-one'][s<2]}.",
    x += 1
print('\n\n'.join(T))
