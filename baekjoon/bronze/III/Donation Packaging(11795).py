A = B = C = 0
for _ in ' '*int(input()):
    a, b, c = map(int, input().split())
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
