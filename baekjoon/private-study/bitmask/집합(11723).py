import sys
S = 0
input()
for l in sys.stdin:
    c, *A = l.split()
    x, y = c[2], 1 << int(*A)
    if'd' == x:
        S |= y
    if'm' == x:
        S &= ~y
    if'e' == x:
        print(+(S & y > 0))
    if'g' == x:
        S ^= y
    if'l' == x:
        S = (1 << 21)-1
    if'p' == x:
        S = 0
