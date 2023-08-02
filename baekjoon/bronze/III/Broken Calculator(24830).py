A = 1
for l in [*open(0)][1:]:
    a, b, c = l.split()
    a, c, x = int(a), int(c), eval(l)
    A = [[[(a+a % 2)//2, x*x][b == '*'], x*A][b == '-'], x-A][b == '+']
    print(A)
