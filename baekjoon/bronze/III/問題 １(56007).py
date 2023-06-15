A = B = 0
for l in [*open(0)][1:]:
    a, b = map(int, l.split())
    if a > b:
        A += a+b
    elif b > a:
        B += a+b
    else:
        A, B = A+a, B+b
print(A, B)
