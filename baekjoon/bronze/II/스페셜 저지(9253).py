I = input
a, b, c = I(), I(), I()
print("YNEOS"[1 ^ (c in a and c in b) :: 2])
