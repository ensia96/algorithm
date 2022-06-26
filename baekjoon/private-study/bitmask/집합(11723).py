S = 0
for _ in ' '*int(input()):
    c, *A = input().split()
    x, y = c[2], A and 1 << int(A[0])
    if x == 'd':
        S |= y
    elif x == 'm':
        S &= ~y
    elif x == 'e':
        print(+bool(S & y))
    elif x == 'g':
        S ^= y
    else:
        S = ((1 << 21)-1)*(x == 'l')
