a = ""
while "#" != a:
    a, b = input().split()
    b = int(b)
    if a in "X#":
        print(A, B)
    elif "B" == a:
        B += b * (B + b < 68)
    elif "C" == a:
        B -= b * (B >= b)
    else:
        A, B = a, b
