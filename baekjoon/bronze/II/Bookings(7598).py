a = ""
while "#" != a:
    a, b = input().split()
    b = int(b)
    if a == "#":
        exit(print(A, B))
    elif a == "X":
        print(A, B)
    elif a == "B":
        B += b * (B + b < 68)
    elif a == "C":
        B -= b * (B >= b)
    else:
        A, B = a, b
