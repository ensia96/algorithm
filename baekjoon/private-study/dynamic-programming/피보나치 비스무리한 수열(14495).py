D = [1]*3
for _ in ' '*113:
    D += D[-1]+D[-3],
print(D[int(input())-1])
