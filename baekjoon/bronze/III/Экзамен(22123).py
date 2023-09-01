i, j = 86400, -3600
for l in [*open(0)][1:]:
    a, b, c = l.split()
    x, y, z = map(int, a.split(':'))
    a = 3600*x+60*y+z
    x, y, z = map(int, b.split(':'))
    b = 3600*x+60*y+z
    c = 60*int(c)
    t = b-a
    t = (t < 1)*i+t-c
    print(['Perfect', ['Test', 'Fail'][t < j]][t < 0])
