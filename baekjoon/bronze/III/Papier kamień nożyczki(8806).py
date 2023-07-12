n, *L = map(float, open(0).read().split())
for i in range(int(n)):
    a, b, c, d, e, f = L[6*i:6*i+6]
    x, y = a*e+b*f+c*d, d*b+e*c+f*a
    print(['=', 'ADAM', 'GOSIA'][(x > y)+2*(x < y)])
