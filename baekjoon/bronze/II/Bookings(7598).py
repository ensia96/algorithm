a = A = ""
B = 0
while "#" != a:
    a, b = input().split()
    b = int(b)
    if a in "X#":
        print(A, B)
        a == "#" and exit()
    elif "B" == a:
        B += b * (B + b < 68)
    elif "C" == a:
        B -= b * (B >= b)
    else:
        A, B = a, b
