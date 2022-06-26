S = 0
for l in [*open(0)][1:]:
    c, *A = l.split()
    x, y = c[2], A and 1 << int(A[0])
    S = {'d': S | y, 'm': S & ~y, 'g': S ^ y, 'e': x ==
         'e' and print(+bool(S & y)) or S}[x]if x in 'dmge'else x == 'l' and (1 << 21)-1
