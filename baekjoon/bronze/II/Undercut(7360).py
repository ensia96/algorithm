*A, _ = open(0)
t = []
for A, B in zip(A[1::3], A[2::3]):
    x = y = 0
    for a, b in zip(A.split(), B.split()):
        a, b = int(a), int(b)
        if a-b == 1:
            y += (a+b)*(1+(a == 2))
        elif b-a == 1:
            x += (a+b)*(1+(b == 2))
        elif a > b:
            x += a
        elif b > a:
            y += b
    t += f"A has {x} points. B has {y} points.",
print('\n\n'.join(t))
