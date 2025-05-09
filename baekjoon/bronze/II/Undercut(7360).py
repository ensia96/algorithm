*A, _ = open(0)
t = []
for A, B in zip(A[1::3], A[2::3]):
    x = y = 0
    for a, b in zip(A.split(), B.split()):
        a, b = int(a), int(b)
        s, u = a+b, abs(a-b) == 1
        a, b = [[max(a, b)*(a != b), s*(1+(s == 3))]
                [u], 0][::1-(2*(u or a < b))]
        x += a
        y += b
    t += f"A has {x} points. B has {y} points.",
print('\n\n'.join(t))
