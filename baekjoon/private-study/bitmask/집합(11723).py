S = 0
for _ in ' '*int(input()):
    c, *A = input().split()
    x, y = c[2], A and 1 << int(A[0])
    S = {'d': S | y, 'm': S & ~y, 'g': S ^ y, 'e': x ==
         'e' and print(+bool(S & y)) or S}[x]if x in 'dmge'else x == 'l' and (1 << 21)-1
