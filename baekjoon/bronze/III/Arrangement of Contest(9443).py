A = 65
for i in sorted([*open(0)][1:]):
    A += i[0] == chr(A)
print(A-65)
