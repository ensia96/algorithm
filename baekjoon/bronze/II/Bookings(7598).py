A, B = "", 0
for l in open(0):
    a, b = l.split()
    b = int(b)
    if a in "X#":
        print(A, B)
    elif a in "B":
        B += b * (B + b < 68)
    elif a == "C":
        B -= b * (B >= b)
    else:
        A, B = a, int(b)
