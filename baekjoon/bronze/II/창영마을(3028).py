T = [1, 0, 0]
for a in input():
    if a == 'A':
        T[0], T[1] = T[1], T[0]
    if a == 'B':
        T[1], T[2] = T[2], T[1]
    if a == 'C':
        T[0], T[2] = T[2], T[0]
print(T.index(1)+1)
