A = B = C = 0
for l in [*open(0)][1:]:
    a, b, c = map(int, l.split())
    A += a
    B += b
    C += c
    if A > 30 and B > 30 and C > 30:
        x = min(A, B, C)
        A -= x
        B -= x
        C -= x
        print(x)
    else:
        print('NO')
