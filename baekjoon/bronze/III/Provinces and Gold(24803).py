g, s, c = map(int, input().split())
x, T = 3*g+2*s+c, []
if x > 7:
    T += 'Province',
elif x > 4:
    T += 'Duchy',
elif x > 1:
    T += 'Estate',
if x > 5:
    T += 'Gold',
elif x > 2:
    T += 'Silver',
else:
    T += 'Copper',
print(' or '.join(T))
